# server/file_handler.py

import os
import base64

FILE_DIR = "received_files"
os.makedirs(FILE_DIR, exist_ok=True)

def save_file(filename, base64_data):
    try:
        file_path = os.path.join(FILE_DIR, filename)
        with open(file_path, 'wb') as f:
            f.write(base64.b64decode(base64_data))
        print(f"[FILE SAVED] {file_path}")
    except Exception as e:
        print(f"[FILE ERROR] {e}")
