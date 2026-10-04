from user import User


class Employee(User):
    def __init__(self, user_id, login, password, name, role, permissions):
        super().__init__(user_id, login, password, name, role, permissions)
