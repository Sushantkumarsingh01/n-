class Admin:
    def __init__(self, admin_id=None, username=None, password=None):
        self._admin_id = admin_id
        self._username = username
        self._password = password


    def get_admin_id(self):
        return self._admin_id

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def set_admin_id(self, admin_id):
        self._admin_id = admin_id

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def __str__(self):
        return f"Admin(ID: {self._admin_id}, Username: {self._username})"


