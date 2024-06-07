
import mysql.connector

DATABASE_NAME = 'nexvega'

def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database=DATABASE_NAME
    )

def create_tables():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        user_id INT PRIMARY KEY,
                        name VARCHAR(100),
                        email VARCHAR(100)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Friendships (
                        user_id INT,
                        friend_id INT,
                        FOREIGN KEY (user_id) REFERENCES Users(user_id),
                        FOREIGN KEY (friend_id) REFERENCES Users(user_id),
                        PRIMARY KEY (user_id, friend_id)
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Recommendations (
                        user_id INT,
                        suggested_friend_id INT,
                        FOREIGN KEY (user_id) REFERENCES Users(user_id),
                        FOREIGN KEY (suggested_friend_id) REFERENCES Users(user_id),
                        PRIMARY KEY (user_id, suggested_friend_id)
                    )''')

    connection.commit()
    connection.close()

def add_user_to_database(user_id, name, email):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (user_id, name, email) VALUES (%s, %s, %s)", (user_id, name, email))
    connection.commit()
    connection.close()

def add_friendship_to_database(user_id, friend_id):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Friendships (user_id, friend_id) VALUES (%s, %s)", (user_id, friend_id))
    cursor.execute("INSERT INTO Friendships (user_id, friend_id) VALUES (%s, %s)", (friend_id, user_id)) 
    connection.commit()
    connection.close()

def store_recommendations(user_id, suggestions):
    connection = get_database_connection()
    cursor = connection.cursor()
    for suggested_friend_id in suggestions:
        cursor.execute("INSERT INTO Recommendations (user_id, suggested_friend_id) VALUES (%s, %s)", (user_id, suggested_friend_id))
    connection.commit()
    connection.close()

create_tables() 