# 💬 Advanced Chat Application (Python + PyQt5 + MySQL)

This is a full-featured chat application built using Python, PyQt5 for GUI, and MySQL for persistent user/message storage. It supports:

- ✅ User registration & login
- 💬 Real-time multi-user messaging
- 😀 Emoji support
- 📎 File/Image sharing
- 🔒 Basic encryption-ready structure
- 🗃️ Chat history per room

## 📁 Folder Structure
    Chat App/
    │
    ├── client/
    │ ├── chat_window.py
    │ ├── client.py
    │ ├── login_window.py
    │ ├── encryption.py
    │ ├── utils.py
    │ ├── config.py
    │ └── file_handler.py
    │
    ├── server/
    │ ├── server.py
    │ ├── client_thread.py
    │ └── db_handler.py


## 🚀 How to Run

    1. ✅ Ensure MySQL is installed and running.
    2. ✅ Create a database `chatapp` and a `users` & `messages` table (already managed in `db_handler.py`).
    3. 💾 Set your MySQL username/password in `config.py`.
    4. ▶️ Start the server:
        python server/server.py

    ▶️ Start the client GUI:
        python client/login_window.py

Register or login, join the general room, chat with emojis, and share files/images!

🧩 Features
    🔐 Secure hashed password storage (SHA-256)

    🎭 Emoji compatibility in messages

    📁 File/image transfer using base64 encoding

    🧠 Multi-threaded server supports multiple clients

    🗂️ Message history loads on room join

    🖼️ GUI made with PyQt5, responsive and easy to use

🔧 Technologies
1. Python 3.x
2. PyQt5
3. MySQL (Connector/Python)
4. Sockets
5. JSON (for structured messaging)

🤝 Contributions
    Feel free to fork and add:
    Voice notes 🎙️ (optional)
    End-to-end encryption 🛡️
    Group creation & private chats
    Dark/light themes

📸 Screenshots
Add login screen, chat room, emoji popup, file send preview screenshots here.

🔹Developer
Name: Jigyanshu Sabata

Internship: OASIS Infobyte

Github: jigyanshuu

📜License
This project is for educational purposes and a requirement for OASIS Infobyte internship.