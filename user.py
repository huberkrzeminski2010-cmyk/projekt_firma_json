class User:
    def __init__(self, user_id, login, password, name, role, permissions):
        self.user_id = user_id
        self.login = login
        self.password = password
        self.name = name
        self.role = role
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions

    def to_dict(self):
        return {
            "id": self.user_id,
            "login": self.login,
            "password": self.password,
            "name": self.name,
            "role": self.role,
            "permissions": self.permissions
        }
