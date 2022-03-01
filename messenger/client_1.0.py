import socket
import json
import threading
import time
from datetime import datetime
import sqlite3


class DB:
    def __init__(self):
        self.db = sqlite3.connect('client.db')
        self.cursor = self.db.cursor()

    def save_msg_in_db(self, sender_name, recipient_name, message, timestamp):

        try:
            self.cursor.execute(
                "INSERT INTO user_messages (sender_name, recipient_name, message, timestamp) VALUES (?,?,?,?)",
                (sender_name, recipient_name, message, timestamp))
            self.cursor.execute("COMMIT;")


        except:
            print('Error adding message into client DB')
        else:
            pass

            # content = jsonBuilder(({'sender': sender, 'for': _for, 'text': text, 'timestamp': timestamp}))
            # print(request(content))

    def is_exists_in_db(self, timestamp):
        self.cursor.execute("SELECT EXISTS (SELECT 1 FROM user_messages WHERE timestamp=?)", (timestamp,))
        out = self.cursor.fetchall()[0][0]
        return True if out == 1 else False

    def __del__(self):
        self.db.close()
        print('db connection closed')


def jsonBuilder(s):
    return json.dumps(s)


def request(content):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 15070))
    print('content=', content)
    sock.send(bytes(content, 'utf-8'))
    response = sock.recv(1024)
    result = response.decode()
    sock.close()
    return result



def connection(user_name, user_password):
    content = jsonBuilder(({'register': user_name, 'user_password': user_password}))

    print(request(content))

def delete_saved_message_from_server(user_name, timestamp):
    content = jsonBuilder(({'delete': user_name, 'timestamp': timestamp}))
    print(request(content))


def send_message(_for, sender, text, timestamp=-1):

    if len(_for) != 0 and len(sender) != 0 and len(text) != 0:
        db.save_msg_in_db(user_name, recipient, message, timestamp)  # save in db message from this client
        content = jsonBuilder(({'sender': sender, 'for': _for, 'text': text, 'timestamp': timestamp}))
        print(request(content))
    else:
        print('Recipient or sender or text is empty. Message not sent.')


def human_readable_time(timestamp):
    msg_time = datetime.fromtimestamp(timestamp)
    time_format = "%Y-%m-%d %H:%M:%S"
    return f"{msg_time:{time_format}}"



def get_message(user_name):
    while True:
        db = DB()
        content = jsonBuilder(({'get': user_name}))
        result = request(content)

        print(result)
        if result != '':
            result = json.loads(result)
            # result = list(result)
            # print('result=', result)
            for i, j, k in result:
                #print(f'{human_readable_time(k)} #  {i}: {j}')
                db.save_msg_in_db(i, user_name, j, k)
                if (db.is_exists_in_db(k)) == True: # is_data_saved_in_db
                    print('hh')
                    delete_saved_message_from_server(user_name, k)



        else:
            print('no messages')
        #     print(f"{result['sender']}: {result['message']}")
        #     # print(" %45 " % (Fore.GREEN + result + Fore.RESET))
        time.sleep(8)

db = DB()

user_name = ''
user_password = ''
register_cycle_break = False
while register_cycle_break == False:
    user_name = input('Enter username:')
    user_password = input('Enter passwords:')
    is_exists = request(jsonBuilder(({'register': user_name, 'user_password': user_password})))
    if is_exists != '"user_exists"':
        register_cycle_break = True
    else:
        print('user_name already busy')

print(user_name)
print(user_password)
#a = (connection(user_name, user_password))








# get_message(user_name)
thread = threading.Thread(target=get_message, args=[user_name])
thread.start()

while True:
    recipient = input('enter recipient name:')
    message = input('Enter message:')
    timestamp = time.time()
    send_message(recipient, user_name, message, timestamp)

