import json

CAMINHO = "persistencia/dados/"

class RegistroDAO:
    def __init__(self):
        self.registros = {}  # Dicionário para armazenar registros
        self.carregar_registros()  # Carrega os registros no início

    def salvar_registros(self):
        registros_data = [
            {"registro": registro, "senha": senha, "tipo": tipo}
            for registro, (senha, tipo) in self.registros.items()
        ]
        with open(CAMINHO + "registros.json", "w", encoding="utf-8") as arquivo:
            json.dump(registros_data, arquivo, indent=4, ensure_ascii=False)

    def carregar_registros(self):
        try:
            with open(CAMINHO + "registros.json", 'r', encoding='utf-8') as arquivo:
                registros_data = json.load(arquivo)
                self.registros = {}
                for dados in registros_data:
                    self.registros[dados['registro']] = (dados['senha'], dados['tipo'])
        except FileNotFoundError:
            self.registros = {}
        except json.JSONDecodeError:
            print("Erro ao carregar registros: arquivo JSON está malformado")
            self.registros = {}

    def adicionar_registro(self, registro, senha, tipo):
        self.registros[registro] = (senha, tipo)
        self.salvar_registros()

    def testar_senha(self, registro, senha):
        if registro in self.registros:
            return self.registros[registro][0] == senha
        return False

    def remover_registro(self, registro):
        if registro in self.registros:
            del self.registros[registro]
            self.salvar_registros()

    def get_tipo(self, registro):
        return self.registros.get(registro, (None, None))[1]
