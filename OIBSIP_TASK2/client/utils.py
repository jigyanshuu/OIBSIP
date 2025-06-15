# utils.py

import os
import base64

# Supported file types
ALLOWED_IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif']
ALLOWED_FILE_EXTENSIONS = ['.pdf', '.txt', '.docx', '.zip'] + ALLOWED_IMAGE_EXTENSIONS

def is_allowed_file(filename):
    _, ext = os.path.splitext(filename.lower())
    return ext in ALLOWED_FILE_EXTENSIONS

def encode_file_to_base64(filepath):
    with open(filepath, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

def decode_base64_to_file(data, output_path):
    with open(output_path, 'wb') as file:
        file.write(base64.b64decode(data))

def apply_emoji_substitutions(message):
    emoji_map = {
        ":)": "😊",
        ":(": "😢",
        "<3": "❤️",
        ":D": "😄",
        ":P": "😛",
        ":o": "😮",
        ":/": "😕",
        ";)": "😉"
    }
    for code, emoji in emoji_map.items():
        message = message.replace(code, emoji)
    return message
