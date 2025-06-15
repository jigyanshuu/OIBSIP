# server/client_thread.py

import threading
import json

class ClientThread(threading.Thread):
    def __init__(self, client_socket, address, db, clients_in_rooms):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.address = address
        self.db = db
        self.clients_in_rooms = clients_in_rooms
        self.username = None
        self.room = None

    def run(self):
        while True:
            try:
                data = self.client_socket.recv(65536).decode('utf-8')
                if not data:
                    break

                try:
                    message = json.loads(data)
                except json.JSONDecodeError:
                    self.send_json({'status': 'error', 'message': 'Invalid JSON format'})
                    continue

                action = message.get('action')

                if action == 'register':
                    username = message.get('username')
                    password = message.get('password')

                    if not username or not password:
                        self.send_json({'status': 'error', 'message': 'Username or password missing'})
                        continue

                    if self.db.user_exists(username):
                        self.send_json({'status': 'error', 'message': 'Username already exists'})
                    else:
                        self.db.create_user(username, password)
                        self.send_json({'status': 'ok', 'message': 'Registration successful'})

                elif action == 'login':
                    username = message.get('username')
                    password = message.get('password')
                    success = self.db.authenticate_user(username, password)
                    if success:
                        self.username = username
                        self.send_json({'status': 'ok'})
                    else:
                        self.send_json({'status': 'error', 'message': 'Invalid credentials'})

                elif action == 'join_room':
                    self.room = message.get('room')
                    self.clients_in_rooms.setdefault(self.room, []).append(self.client_socket)
                    history = self.db.get_messages(self.room)
                    self.send_json({'action': 'history', 'messages': history})

                elif action == 'message':
                    msg = message.get('message')
                    room = message.get('room')
                    self.db.save_message(self.username, room, msg)

                    for client in self.clients_in_rooms.get(room, []):
                        try:
                            payload = {
                                'action': 'message',
                                'from': self.username,
                                'message': msg
                            }
                            client.sendall(json.dumps(payload).encode('utf-8'))
                        except:
                            continue

                elif action == 'file':
                    filename = message.get('filename')
                    room = message.get('room')
                    filedata = message.get('filedata')
                    sender = message.get('from')

                    for client in self.clients_in_rooms.get(room, []):
                        if client != self.client_socket:
                            try:
                                client.sendall(json.dumps({
                                    'action': 'file',
                                    'filename': filename,
                                    'filedata': filedata,
                                    'from': sender
                                }).encode('utf-8'))
                            except:
                                continue

            except Exception as e:
                print(f"[ERROR]: {e}")
                break

        self.client_socket.close()
        if self.room and self.client_socket in self.clients_in_rooms.get(self.room, []):
            self.clients_in_rooms[self.room].remove(self.client_socket)

    def send_json(self, data):
        try:
            self.client_socket.sendall(json.dumps(data).encode('utf-8'))
        except Exception as e:
            print(f"[SEND ERROR]: {e}")
