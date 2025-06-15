# client/chat_window.py

import json
import threading
import os
from PyQt5.QtWidgets import (
    QWidget, QTextEdit, QLineEdit, QVBoxLayout, QPushButton, QLabel,
    QFileDialog, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ChatWindow(QWidget):
    def __init__(self, sock, username):
        super().__init__()
        self.sock = sock
        self.username = username
        self.setWindowTitle(f"Chat - {self.username}")
        self.setGeometry(600, 200, 600, 500)
        self.init_ui()
        self.join_room("general")
        threading.Thread(target=self.listen_for_messages, daemon=True).start()

    def init_ui(self):
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)

        self.message_input = QLineEdit()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        self.emoji_button = QPushButton("😊")
        self.emoji_button.clicked.connect(self.insert_emoji)

        self.file_button = QPushButton("📎")
        self.file_button.clicked.connect(self.send_file)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Chat Room: general"))
        layout.addWidget(self.chat_display)

        hbox = QHBoxLayout()
        hbox.addWidget(self.message_input)
        hbox.addWidget(self.emoji_button)
        hbox.addWidget(self.file_button)
        hbox.addWidget(self.send_button)

        layout.addLayout(hbox)
        self.setLayout(layout)

    def join_room(self, room):
        self.room = room
        join_msg = {'action': 'join_room', 'room': self.room}
        self.sock.sendall(json.dumps(join_msg).encode('utf-8'))

    def insert_emoji(self):
        self.message_input.insert("😊")  # Add your favorite emoji here

    def send_message(self):
        message = self.message_input.text().strip()
        if message:
            data = {
                'action': 'message',
                'message': message,
                'room': self.room
            }
            try:
                self.sock.sendall(json.dumps(data).encode('utf-8'))
            except Exception as e:
                self.chat_display.append(f"[Send Error] {e}")
            self.message_input.clear()

    def send_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                filename = os.path.basename(file_path)
                data = {
                    'action': 'file',
                    'filename': filename,
                    'room': self.room,
                    'from': self.username,
                    'filedata': content.decode('latin1')  # Use latin1 to preserve binary format
                }
                self.sock.sendall(json.dumps(data).encode('utf-8'))
                self.chat_display.append(f"[You sent a file] {filename}")
            except Exception as e:
                self.chat_display.append(f"[File Send Error] {e}")

    def listen_for_messages(self):
        while True:
            try:
                data = self.sock.recv(65536).decode('utf-8')
                if not data:
                    break
                msg = json.loads(data)
                if msg['action'] == 'message':
                    sender = msg['from']
                    text = msg['message']
                    self.chat_display.append(f"{sender}: {text}")
                elif msg['action'] == 'history':
                    for m in msg['messages']:
                        self.chat_display.append(f"{m['sender']}: {m['message']}")
                elif msg['action'] == 'file':
                    filename = msg['filename']
                    sender = msg['from']
                    filedata = msg['filedata'].encode('latin1')
                    save_path = os.path.join("downloads", filename)
                    os.makedirs("downloads", exist_ok=True)
                    with open(save_path, "wb") as f:
                        f.write(filedata)
                    self.chat_display.append(f"[File received from {sender}]: {filename} (saved to downloads/)")
            except Exception as e:
                self.chat_display.append(f"[Error receiving message] {e}")
                break
