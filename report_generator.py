from datetime import datetime


class ReportGenerator:
    def __init__(self, company):
        self.company = company

    def generate_report(self, file_name):
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(f"Raport firmy: {self.company.name}\n")
                file.write(f"Data wygenerowania: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("\n")

                file.write("UZYTKOWNICY:\n")
                for user in self.company.users:
                    file.write(f"- ID: {user.user_id}\n")
                    file.write(f"  Login: {user.login}\n")
                    file.write(f"  Imie i nazwisko: {user.name}\n")
                    file.write(f"  Rola: {user.role}\n")
                    file.write(f"  Uprawnienia: {', '.join(user.permissions)}\n")

                file.write("\nPRODUKTY:\n")
                for product in self.company.products:
                    file.write(f"- ID: {product.product_id}\n")
                    file.write(f"  Nazwa: {product.name}\n")
                    file.write(f"  Cena: {product.price} zl\n")
                    file.write(f"  Ilosc w magazynie: {product.quantity}\n")

                file.write("\nFINANSE FIRMY:\n")
                file.write(f"Stan konta: {self.company.finance.balance} zl\n")
                file.write(f"Przychody: {self.company.finance.income} zl\n")
                file.write(f"Wydatki: {self.company.finance.expenses} zl\n")

            print(f"Wygenerowano raport: {file_name}")
        except OSError:
            print("Nie udalo sie wygenerowac raportu.")
