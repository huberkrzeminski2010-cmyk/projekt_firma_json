from admin import Admin
from employee import Employee
from finance import Finance
from product import Product


class Company:
    def __init__(self, name, storage):
        self.name = name
        self.storage = storage
        self.users = []
        self.products = []
        self.finance = None

    def load_data(self):
        users_data = self.storage.load("users.json")
        products_data = self.storage.load("products.json")
        finance_data = self.storage.load("finance.json")

        if users_data is None or products_data is None or finance_data is None:
            return False

        self.users = []
        for user_data in users_data:
            if user_data["role"] == "admin":
                user = Admin(
                    user_data["id"],
                    user_data["login"],
                    user_data["password"],
                    user_data["name"],
                    user_data["permissions"]
                )
            else:
                user = Employee(
                    user_data["id"],
                    user_data["login"],
                    user_data["password"],
                    user_data["name"],
                    user_data["role"],
                    user_data["permissions"]
                )
            self.users.append(user)

        self.products = []
        for product_data in products_data:
            product = Product(
                product_data["id"],
                product_data["name"],
                product_data["price"],
                product_data["quantity"]
            )
            self.products.append(product)

        self.finance = Finance(
            finance_data["balance"],
            finance_data["income"],
            finance_data["expenses"]
        )
        return True

    def save_data(self):
        self.storage.save("users.json", [user.to_dict() for user in self.users])
        self.storage.save("products.json", [product.to_dict() for product in self.products])
        self.storage.save("finance.json", self.finance.to_dict())

    def login(self, login, password):
        for user in self.users:
            if user.login == login and user.password == password:
                return user
        return None

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def sell_product(self, product_id, quantity):
        product = self.find_product_by_id(product_id)

        if product is None:
            return "Nie znaleziono produktu."

        if quantity <= 0:
            return "Ilosc musi byc wieksza od zera."

        if product.quantity < quantity:
            return "Brak wystarczajacej liczby produktow."

        product.quantity -= quantity
        self.finance.add_income(product.price * quantity)
        self.save_data()
        return "Sprzedaz zakonczona sukcesem."

    def order_product(self, product_id, quantity):
        product = self.find_product_by_id(product_id)

        if product is None:
            return "Nie znaleziono produktu."

        if quantity <= 0:
            return "Ilosc musi byc wieksza od zera."

        cost = product.price * quantity * 0.6
        product.quantity += quantity
        self.finance.add_expense(cost)
        self.save_data()
        return "Zamowienie zakonczone sukcesem."
