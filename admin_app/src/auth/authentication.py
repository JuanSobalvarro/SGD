# src/auth/authentication.py
import hashlib


class AuthService:
    def __init__(self):
        # md5 hash for users
        self.users = {
            'admin': '21232f297a57a5a743894a0e4a801fc3',  # admin
            'esther': "924728f24158c0beef3ee10021497d3c",  # purrungaanonima
        }

    def authenticate(self, username, password):
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        return self.users.get(username) == hashed_password

    def add_user(self, username, password):
        self.users[username] = hashlib.md5(password.encode()).hexdigest()

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
