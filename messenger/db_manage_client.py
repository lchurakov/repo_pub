import sqlite3
# create db+table users_db
# sqlite_connection = sqlite3.connect('client.db')
# cursor = sqlite_connection.cursor()
# cursor.execute("""create table client_params (
#                client_user_name TEXT UNIQUE,
#                client_password TEXT NOT NULL,
#                client_secret_key TEXT NOT NULL,
#                server_secret_key TEXT NOT NULL
#                )
#                """)
# cursor.close()
#
# create table users_messages
# sqlite_connection = sqlite3.connect('client.db')
# cursor = sqlite_connection.cursor()
# cursor.execute("""create table user_messages (
#                sender_name TEXT NOT NULL,
#                recipient_name TEXT NOT NULL,
#                message TEXT NOT NULL,
#                timestamp FLOAT NUT NULL UNIQUE)
#                """)
# cursor.close()

# # delete all from user_messages:
# sqlite_connection = sqlite3.connect('client.db')
# cursor = sqlite_connection.cursor()
# cursor.execute("DELETE FROM user_messages")
# cursor.execute("COMMIT;")
# cursor.close()

# # delete table user_messages:
# sqlite_connection = sqlite3.connect('client.db')
# cursor = sqlite_connection.cursor()
# cursor.execute("""DROP TABLE user_messages""")
# cursor.close()

timestamp = 1645343665.3712656
user_name = 'admin'

# # delete all from user_messages:
sqlite_connection = sqlite3.connect('client.db')
cursor = sqlite_connection.cursor()
cursor.execute("DELETE FROM user_messages WHERE recipient_name=? and timestamp =?", (user_name, timestamp,))
cursor.execute("COMMIT;")
cursor.close()


