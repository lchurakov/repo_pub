import sqlite3
# create db+table users_db
# sqlite_connection = sqlite3.connect('server.db')
# cursor = sqlite_connection.cursor()
# cursor.execute("""create table users_db (
#                user_id INTEGER PRIMARY KEY,
#                user_name TEXT NOT NULL UNIQUE,
#                user_password TEXT NOT NULL)
#                """)
# cursor.close()
#
# # create table users_messages
# sqlite_connection = sqlite3.connect('server.db')
# cursor = sqlite_connection.cursor()
# cursor.execute("""create table user_messages (
#                sender_name TEXT NOT NULL,
#                recipient_name TEXT NOT NULL,
#                message TEXT NOT NULL,
#                timestamp FLOAT NOT NULL)
#                """)
# cursor.close()

# # delete all from users_db
# sqlite_connection = sqlite3.connect('server.db')
# cursor = sqlite_connection.cursor()
# cursor.execute("""DELETE FROM users_db
#                """)
# cursor.close()

# # delete table user_messages
# sqlite_connection = sqlite3.connect('server.db')
# cursor = sqlite_connection.cursor()
# cursor.execute("""DROP TABLE user_messages
#                """)
# cursor.execute('COMMIT;')
# cursor.close()

user_name = 'admin'

sqlite_connection = sqlite3.connect('server.db')
cursor = sqlite_connection.cursor()
cursor.execute("SELECT 1 FROM users_db WHERE user_name=?", (user_name,))
#cursor.execute("SELECT EXISTS (SELECT 1 FROM users_db WHERE user_name =?)",(user_name))
print(cursor.fetchall())
cursor.close()



#cursor.execute("SELECT user_name FROM user_db WHERE EXISTS (SELECT user_name FROM users_db WHERE user_name=admin")

