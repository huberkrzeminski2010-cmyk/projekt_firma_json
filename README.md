# Projekt Python: firma z zapisem JSON

Prosty projekt szkolny zgodny z wymaganiami:

- kod jest podzielony na oddzielne pliki,
- jedna klasa znajduje sie w jednym pliku,
- dane programu sa zapisywane tylko w plikach JSON,
- program ma logowanie dla administratora i dwoch pracownikow,
- zastosowano `try/except`,
- administrator moze zmieniac dane i uprawnienia uzytkownikow,
- zastosowano dziedziczenie oraz kompozycje,
- program obsluguje produkty, sprzedaz, zamawianie i finanse firmy,
- program generuje raport tekstowy z danymi firmy.

## Uruchomienie

1. Otworz terminal w folderze projektu.
2. Uruchom:

```bash
python main.py
```

Nie trzeba instalowac dodatkowych bibliotek.

## Przykladowe loginy

| Login | Haslo | Opis |
| --- | --- | --- |
| admin | admin123 | Administrator |
| kasjer | kasjer123 | Pracownik moze sprzedawac i generowac raport |
| magazyn | magazyn123 | Pracownik moze zamawiac produkty |

## Pliki JSON

Dane programu znajduja sie w folderze `data`:

- `users.json` - uzytkownicy, hasla, role i uprawnienia,
- `products.json` - produkty, ceny i ilosci,
- `finance.json` - stan finansow firmy.

## Dziedziczenie

Klasa `Admin` i klasa `Employee` dziedzicza po klasie `User`.

## Kompozycja

Klasa `Company` korzysta z obiektow innych klas:

- `JsonStorage`,
- `Product`,
- `Finance`,
- `Admin`,
- `Employee`.

## Raport

Raport mozna wygenerowac z menu programu. Powstanie plik:

```text
raport_firmy.txt
```

Raport jest zwyklym plikiem tekstowym, ale nie jest magazynem danych programu. Dane programu sa trzymane w JSON.
