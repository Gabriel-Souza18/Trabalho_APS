import json


class BaseDAO:
    def __init__(self, file_name):
        self.file_path = "persistencia/dados/" + file_name
        self.data = {}
        self.load_data()

    def salvar_data(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def load_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
                if not isinstance(self.data, dict):  # Verifica se os dados são um dicionário
                    self.data = {}
        except FileNotFoundError:
            pass

    def add_item(self, key, item):
        self.data[key] = item
        self.salvar_data()

    def remove_item(self, key):
        if key in self.data:
            del self.data[key]
            self.salvar_data()

    def get_item(self, key):
        return self.data.get(key)
