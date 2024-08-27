import os
import random
import string
import base64

def random_string(string_length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

def base64_encode_username_password(username, password):
    sample_string = username + ":" + password
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

def base64_decode_username_password(s):
    base64_string = s
    base64_bytes = base64_string.encode("ascii")

    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    username_password = sample_string.split(":")
    if len(username_password) != 2:
        return []
    else:
        return username_password

def get_size(file_path):
    file_size = os.path.getsize(file_path)
    size = file_size / 1024 ** 2
    return round(size, 3)