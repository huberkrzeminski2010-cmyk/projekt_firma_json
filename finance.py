class Finance:
    def __init__(self, balance, income, expenses):
        self.balance = balance
        self.income = income
        self.expenses = expenses

    def add_income(self, amount):
        self.balance += amount
        self.income += amount

    def add_expense(self, amount):
        self.balance -= amount
        self.expenses += amount

    def to_dict(self):
        return {
            "balance": self.balance,
            "income": self.income,
            "expenses": self.expenses
        }
