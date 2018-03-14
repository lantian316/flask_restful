from werkzeug.security import safe_str_cmp
from usermanage import FindUser

finder = FindUser(db='data.db')

def authenticate(username, password):
    users = finder.find_by_username(username)
    if users:
        for user in users:
            if safe_str_cmp(user.password, password):
                return user


def identity(payload):
    user_id = payload['identity']
    return finder.find_by_id(user_id)