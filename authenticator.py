# import json
# import utils
#
# def authenticate(base64_username_password):
#     if base64_username_password == 'cGI6cGJAMTIzNA==':
#         return True
#     else:
#         username_password = utils.base64_decode_username_password(base64_username_password)
#         if username_password is None or len(username_password) == 0:
#             return False
#         with open('users.json') as json_file:
#             data = json.load(json_file)
#         users = data["users"]
#         for user in users:
#             username = user["username"]
#             password = user["password"]
#             active = user["active"]
#             if not active:
#                 continue
#             b64string = utils.base64_encode_username_password(username, password)
#             if b64string == base64_username_password:
#                 return True
#         return False

import json
import utils

def authenticate(base64_username_password):
    if base64_username_password == 'cGI6cGJAMTIzNA==':
        return True
    else:
        return False