class User:
    def __init__(self, username):
        self.username = username
        self.is_authenticated = False

    def authenticate(self):
        self.is_authenticated = True

    def logout(self):
        self.is_authenticated = False
