# client/client.py

import socket
import json
from chat_window import ChatWindow
from PyQt5.QtWidgets import QApplication

class ChatClient:
    def __init__(self, username):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', 5555))
        self.username = username

    def login(self):
        data = {
            'action': 'login',
            'username': self.username,
            'password': self.username  # Simplified for demo; use real input in production
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        response = self.sock.recv(4096).decode('utf-8')
        return json.loads(response)

    def run(self):
        app = QApplication([])
        window = ChatWindow(self.sock, self.username)
        window.show()
        app.exec_()
