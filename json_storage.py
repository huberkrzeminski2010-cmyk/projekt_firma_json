import json
from pathlib import Path


class JsonStorage:
    def __init__(self, data_folder):
        self.data_folder = Path(data_folder)

    def load(self, file_name):
        file_path = self.data_folder / file_name

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Nie znaleziono pliku: {file_path}")
            return None
        except json.JSONDecodeError:
            print(f"Plik {file_path} ma bledny format JSON.")
            return None

    def save(self, file_name, data):
        file_path = self.data_folder / file_name

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except OSError:
            print(f"Nie udalo sie zapisac pliku: {file_path}")
