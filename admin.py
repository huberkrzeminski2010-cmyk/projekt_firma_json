from user import User


class Admin(User):
    def __init__(self, user_id, login, password, name, permissions):
        super().__init__(user_id, login, password, name, "admin", permissions)

    def change_user_data(self, user, new_name, new_role, new_permissions):
        user.name = new_name
        user.role = new_role
        user.permissions = new_permissions
