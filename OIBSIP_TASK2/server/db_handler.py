# server/db_handler.py

import mysql.connector
import hashlib
import datetime

class DBHandler:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Jigyanshu07",  # Change to your MySQL password
            database="chatapp"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def user_exists(self, username):
        self.cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        return self.cursor.fetchone() is not None

    def create_user(self, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", 
                            (username, password_hash))
        self.connection.commit()

    def authenticate_user(self, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute(
            "SELECT id FROM users WHERE username = %s AND password_hash = %s", 
            (username, password_hash)
        )
        return self.cursor.fetchone() is not None

    def save_message(self, sender, room, message):
        timestamp = datetime.datetime.now()
        self.cursor.execute(
            "INSERT INTO messages (sender, room, message, timestamp) VALUES (%s, %s, %s, %s)",
            (sender, room, message, timestamp)
        )
        self.connection.commit()

    def save_file(self, sender, room, filename, file_data):
        timestamp = datetime.datetime.now()
        self.cursor.execute(
            "INSERT INTO files (sender, room, filename, file_data, timestamp) VALUES (%s, %s, %s, %s, %s)",
            (sender, room, filename, file_data, timestamp)
        )
        self.connection.commit()

    def get_messages(self, room):
        self.cursor.execute(
            "SELECT sender, message, timestamp FROM messages WHERE room = %s ORDER BY timestamp ASC",
            (room,)
        )
        return self.cursor.fetchall()

    def get_files(self, room):
        self.cursor.execute(
            "SELECT sender, filename, file_data, timestamp FROM files WHERE room = %s ORDER BY timestamp ASC",
            (room,)
        )
        return self.cursor.fetchall()
