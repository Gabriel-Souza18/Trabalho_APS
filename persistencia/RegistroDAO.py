import json

from persistencia.BaseDAO import BaseDAO


class RegistroDAO(BaseDAO):
    def __init__(self):
        super().__init__("registros.json")
        self.data = self.carregar_registros()  # Carrega os registros no início

    def salvar_registros(self):
        registros_data = [
            {"registro": registro, "senha": senha, "tipo": tipo}
            for registro, (senha, tipo) in self.data.items()
        ]
        with open(self.file_path, "w", encoding="utf-8") as arquivo:
            json.dump(registros_data, arquivo, indent=4, ensure_ascii=False)

    def carregar_registros(self):

        try:
            with open(self.file_path, 'r', encoding='utf-8') as arquivo:
                registros_data = json.load(arquivo)
                registros = {}
                for dados in registros_data:
                    self.data[dados['registro']] = (dados['senha'], dados['tipo'])

                return self.data
        except FileNotFoundError:

            return {}
        except json.JSONDecodeError:
            print("Erro ao carregar registros: arquivo JSON está malformado")

            return {}

    def adicionar_registro(self, registro, senha, tipo):
        self.add_item(registro, {"senha": senha, "tipo": tipo})
        self.salvar_registros()

    def testar_senha(self, registro, senha):
        if registro in self.data:
            return self.data[registro][0] == senha
        return False

    def remover_registro(self, registro):
        self.remove_item(registro)

    def get_tipo(self, registro):
        return self.data.get(registro, (None, None))[1]
