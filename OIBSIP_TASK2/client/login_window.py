# client/login_window.py

import sys
import json
import socket
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from chat_window import ChatWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.sock = None
        self.setWindowTitle("Login")
        self.setGeometry(600, 300, 300, 200)
        self.init_ui()

    def init_ui(self):
        self.label1 = QLabel("Username:")
        self.username_input = QLineEdit()
        self.label2 = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("Register")

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.username_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('127.0.0.1', 5555))
            data = {
                'action': 'login',
                'username': username,
                'password': password
            }
            self.sock.sendall(json.dumps(data).encode('utf-8'))
            response = json.loads(self.sock.recv(4096).decode('utf-8'))

            if response.get('status') == 'ok':
                self.open_chat(username)
            else:
                QMessageBox.critical(self, "Error", response.get('message', 'Unknown error'))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to communicate with server: {e}")

    def register(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('127.0.0.1', 5555))
            data = {
                'action': 'register',
                'username': username,
                'password': password
            }
            self.sock.sendall(json.dumps(data).encode('utf-8'))
            response = json.loads(self.sock.recv(4096).decode('utf-8'))

            if response.get('status') == 'ok':
                QMessageBox.information(self, "Success", "Registered successfully!")
            else:
                QMessageBox.warning(self, "Warning", response.get('message'))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to communicate with server: {e}")

    def open_chat(self, username):
        self.chat = ChatWindow(self.sock, username)
        self.chat.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
