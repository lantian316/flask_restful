import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE USERS (ID INT PRIMARY KEY NOT NULL, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL);"
cursor.execute('''CREATE TABLE USERS
         (ID INT PRIMARY KEY     NOT NULL,
         USERNAME           TEXT    NOT NULL,
         PASSWORD       TEXT     NOT NULL);''')

user_1 = (1, 'nam', '1')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user_1)

users = [
    (2, 'nam1', '2'),
    (3, 'nam2', '1'),
    (4, 'nam3', '1')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM USERS;"
for row in cursor.execute(select_query):
    print(row)

connection.commit()


connection.close()