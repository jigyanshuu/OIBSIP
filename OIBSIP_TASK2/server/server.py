# server/server.py

import socket
from db_handler import DBHandler
from client_thread import ClientThread

HOST = '127.0.0.1'
PORT = 5555

def main():
    db = DBHandler()
    clients_in_rooms = {}

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[INFO] Server listening on {HOST}:{PORT}")

    try:
        while True:
            client_sock, addr = server_socket.accept()
            print(f"[NEW CONNECTION] {addr} connected.")
            thread = ClientThread(client_sock, addr, db, clients_in_rooms)
            thread.start()
    except KeyboardInterrupt:
        print("\n[INFO] Shutting down server...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
