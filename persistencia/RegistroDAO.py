import json
from persistencia.BaseDAO import BaseDAO

class RegistroDAO(BaseDAO):
    def __init__(self):
        super().__init__("registros.json")
        self.registros = self.carregar_registros()  # Carrega os registros no início

    def carregar_registros(self):
        registros = {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                dados = json.load(file)
                if isinstance(dados, list):
                    for item in dados:
                        registros[item['registro']] = (item['senha'], item['tipo'])
                elif isinstance(dados, dict):
                    for registro, item in dados.items():
                        registros[registro] = (item['senha'], item['tipo'])
        except FileNotFoundError:
            self.registros = {}
        except json.JSONDecodeError:
            print("Erro ao carregar registros: arquivo JSON está malformado")
            self.registros = {}
        return registros

    def salvar_registros(self):
        registros_para_salvar = {
            reg: {"senha": dados[0], "tipo": dados[1]}
            for reg, dados in self.registros.items()
        }
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(registros_para_salvar, file, indent=4, ensure_ascii=False)

    def adicionar_registro(self, registro, senha, tipo):
        self.registros[registro] = (senha, tipo)
        self.salvar_registros()  # Salvar alterações no arquivo JSON

    def remover_registro(self, registro):
        if registro in self.registros:
            del self.registros[registro]
            self.salvar_registros()  # Salvar alterações no arquivo JSON

    def testar_senha(self, registro, senha):
        # Verifica se o registro existe e se a senha está correta
        if registro in self.registros:
            return self.registros[registro][0] == senha
        return False

    def get_tipo(self, registro):
        # Retorna o tipo associado ao registro, se existir
        return self.registros.get(registro, (None, None))[1]

    def buscar_registros(self):
        # Retorna todos os registros
        return self.registros.values()
