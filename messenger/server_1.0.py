from socketserver import *
import json
import sqlite3
import time
#import server_crypt
#import test_module  # модуль unit-тестов
#import checkings  # модуль проверок на ошибки сервера

host = '127.0.0.1'
port = 15070
addr = (host, port)


class Server:
    def main_parameters(self):
        # self.host = '127.0.0.1'
        # self.port = 15053
        pass


class DB:
    def __init__(self):
        self.db = sqlite3.connect('server.db')
        self.cursor = self.db.cursor()

    def is_user_exists(self, user_name):
        #self.cursor.execute("SELECT EXSIST (SELECT 1 FROM users_db WHERE user_name=?)", (username))
        self.cursor.execute("SELECT 1 FROM users_db WHERE user_name=?", (user_name,))
        is_exists = self.cursor.fetchall()
        print('is_exists=', is_exists)
        return True if len(is_exists) != 0 and is_exists[0][0] == 1 else False

            #return True if self.cursor.fetchall()[0][0] == 1 else False

    def user_login(self, user_name, user_password):

        self.cursor.execute("SELECT EXSIST (SELECT 1 FROM users_db WHERE user_name=? AND user_password=?)",
                            (user_name, user_password))
        print(self.cursor.fetchall())
        # TODO: cursor.execute("SELECT EXISTS (SELECT 1 FROM users_db WHERE user_name=?)", (username,))
        #     print(cursor.fetchall())
        #  сюда лучше подойдет

    def save_msg_in_db(self, sender_name, recipient_name, message, timestamp):
        self.cursor.execute("INSERT INTO user_messages (sender_name, recipient_name, message, timestamp) VALUES (?,?,?,?)",
                            (sender_name, recipient_name, message, timestamp))
        self.cursor.execute("COMMIT;")

    def query_msg_from_db(self, username):
        self.cursor.execute("SELECT sender_name, message, timestamp FROM user_messages WHERE recipient_name=?", (username,))
        # TODO: delete messages after transfer to client
        return self.cursor.fetchall()

    def delete_msg_from_db(self, username, timestamp):
        self.cursor.execute("DELETE FROM user_messages WHERE recipient_name=? AND timestamp =?", (username, timestamp,))
        self.cursor.execute("COMMIT;")

    def users_insert(self, username, user_password):
        try:
            self.cursor.execute("INSERT INTO users_db (user_name, user_password) VALUES (?,?)",
                                (username, user_password))
            self.cursor.execute("COMMIT;")
        except sqlite3.IntegrityError:
            return f'user {username} already exists'
            # todo: send error to client
        else:
            return f'user {username} successfully added in DB'

    def __del__(self):
        self.db.close()




class MyTCPHandler(StreamRequestHandler):
    def jsonBuilder(self, data):
        return json.dumps(data)



    def handle(self):
        data = self.request.recv(1024).strip()
        decoded_data = json.loads(data.decode())
        print('decoded_data=',decoded_data)

        if decoded_data.get('login') is not None:
            # user_names.append(decoded_data.get('user_name'))
            db.user_login(decoded_data.get('user_name'))

            user_name = decoded_data.get('login')
            user_password = decoded_data.get('user_password')
            # print(db.users_insert(decoded_data.get('user_name')))
            # db.users_insert(decoded_data.get('user_name'))
        if decoded_data.get('register') is not None:
            user_name = decoded_data.get('register')
            user_password = decoded_data.get('user_password')

            if db.is_user_exists(user_name):
                # send: user_exists

                # content = self.jsonBuilder(({'sender': data_from_db[0][0], 'message': data_from_db[0][1]}))
                content = self.jsonBuilder(('user_exists'))
                self.request.sendall(bytes(content, 'utf-8'))
                pass
            else:
                print(db.users_insert(user_name, user_password))

        # user_name = decoded_data.get('user_name')
        # if user_name is not None:
        #     user_names.append(user_name)

        if decoded_data.get('delete') is not None:
            user_name = decoded_data.get('delete')
            timestamp = decoded_data.get('timestamp')
            db.delete_msg_from_db(user_name, timestamp)

        if decoded_data.get('get') is not None:
            # user_get_messages_request = decoded_data.get('get')
            # print(user_get_messages_request)
            print('data from db:', db.query_msg_from_db(decoded_data.get('get')))
            data_from_db = db.query_msg_from_db(decoded_data.get('get'))



            if len(data_from_db) != 0:
                # print('---')
                # print(data_from_db)
                # print('---')
                sender = data_from_db[0][0]
                message = data_from_db[0][1]

                # print('sender', sender)
                # print('message', message)
                #
                # print('len=', len(data_from_db))
                # print('---')

                # di = dict()
                # for i, j in data_from_db:
                #     di[i] = j
                # print(di)
                # content = self.jsonBuilder(({'sender': data_from_db[0][0], 'message': data_from_db[0][1]}))
                content = self.jsonBuilder(data_from_db)
                self.request.sendall(bytes(content, 'utf-8'))



            else:
                # self.request.sendall(bytes(-1, 'utf-8'))
                print('no messages')

            # print(db.query_msg_from_db(decoded_data.get('get')))
            # self.request.sendall((db.query_msg_from_db(decoded_data.get('get'))))
            # content = self.jsonBuilder(({'sender': user_name, 'user_password': user_password}))
            #
            # self.request.sendall(b'hi')

        if decoded_data.get('for') is not None:

            sender_name = decoded_data.get('sender')
            recipient_name = decoded_data.get('for')
            message = decoded_data.get('text')
            timestamp = decoded_data.get('timestamp')
            if recipient_name == 'server':
                print('recipient: ',recipient_name, 'sender:',sender_name)

            db.save_msg_in_db(sender_name, recipient_name, message, timestamp)

        # print('client send:' + str(self.data))

        # self.request.sendall(b'Hello from server!')


if __name__ == '__main__':
    db = DB()

    server = TCPServer(addr, MyTCPHandler)
    print('Starting server...')
    server.serve_forever()
