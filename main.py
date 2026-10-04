from pathlib import Path

from company import Company
from json_storage import JsonStorage
from report_generator import ReportGenerator


DATA_FOLDER = Path(__file__).parent / "data"


def show_products(company):
    print("\nProdukty:")
    for product in company.products:
        print(f"{product.product_id}. {product.name} | cena: {product.price} zl | ilosc: {product.quantity}")


def show_users(company):
    print("\nUzytkownicy:")
    for user in company.users:
        print(f"{user.user_id}. {user.login} | {user.name} | rola: {user.role} | uprawnienia: {user.permissions}")


def admin_menu(company, user):
    while True:
        print("\n--- MENU ADMINA ---")
        print("1. Pokaz uzytkownikow")
        print("2. Zmien dane i uprawnienia uzytkownika")
        print("3. Pokaz produkty")
        print("4. Wygeneruj raport")
        print("0. Wyloguj")

        choice = input("Wybierz opcje: ")

        if choice == "1":
            show_users(company)
        elif choice == "2":
            try:
                user_id = int(input("Podaj ID uzytkownika: "))
                selected_user = company.find_user_by_id(user_id)

                if selected_user is None:
                    print("Nie znaleziono uzytkownika.")
                    continue

                new_name = input("Nowe imie i nazwisko: ")
                new_role = input("Nowa rola: ")
                permissions_text = input("Uprawnienia po przecinku, np. sell,order: ")
                new_permissions = [item.strip() for item in permissions_text.split(",") if item.strip()]

                user.change_user_data(selected_user, new_name, new_role, new_permissions)
                company.save_data()
                print("Dane uzytkownika zostaly zmienione.")
            except ValueError:
                print("ID musi byc liczba.")
        elif choice == "3":
            show_products(company)
        elif choice == "4":
            report_path = Path(__file__).parent / "raport_firmy.txt"
            ReportGenerator(company).generate_report(report_path)
        elif choice == "0":
            break
        else:
            print("Nie ma takiej opcji.")


def employee_menu(company, user):
    while True:
        print("\n--- MENU PRACOWNIKA ---")
        print("1. Pokaz produkty")
        print("2. Sprzedaj produkt")
        print("3. Zamow produkt")
        print("4. Wygeneruj raport")
        print("0. Wyloguj")

        choice = input("Wybierz opcje: ")

        if choice == "1":
            show_products(company)
        elif choice == "2":
            if not user.has_permission("sell"):
                print("Nie masz uprawnien do sprzedazy.")
                continue

            try:
                product_id = int(input("Podaj ID produktu: "))
                quantity = int(input("Podaj ilosc: "))
                print(company.sell_product(product_id, quantity))
            except ValueError:
                print("ID produktu i ilosc musza byc liczbami.")
        elif choice == "3":
            if not user.has_permission("order"):
                print("Nie masz uprawnien do zamawiania.")
                continue

            try:
                product_id = int(input("Podaj ID produktu: "))
                quantity = int(input("Podaj ilosc: "))
                print(company.order_product(product_id, quantity))
            except ValueError:
                print("ID produktu i ilosc musza byc liczbami.")
        elif choice == "4":
            if not user.has_permission("report"):
                print("Nie masz uprawnien do raportow.")
                continue

            report_path = Path(__file__).parent / "raport_firmy.txt"
            ReportGenerator(company).generate_report(report_path)
        elif choice == "0":
            break
        else:
            print("Nie ma takiej opcji.")


def main():
    storage = JsonStorage(DATA_FOLDER)
    company = Company("Sklep Szkolny Python", storage)

    if not company.load_data():
        print("Nie udalo sie wczytac danych programu.")
        return

    print("=== SYSTEM FIRMY ===")
    login = input("Login: ")
    password = input("Haslo: ")

    user = company.login(login, password)

    if user is None:
        print("Bledny login lub haslo.")
        return

    print(f"Zalogowano jako: {user.name} ({user.role})")

    if user.role == "admin":
        admin_menu(company, user)
    else:
        employee_menu(company, user)


if __name__ == "__main__":
    main()
