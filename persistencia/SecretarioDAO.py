import json
from modelo.pessoas.Secretario import Secretario
from persistencia.BaseDAO import BaseDAO

class SecretarioDAO(BaseDAO):
    def __init__(self):
        super().__init__("secretarios.json")
        self.secretarios = self.carregar_secretarios()

    def carregar_secretarios(self):
        secretarios = {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as arquivo:
                self.data = json.load(arquivo)
                for dados in self.data:
                    secretario = Secretario(
                        dados['nome'],
                        dados['idade'],
                        dados['email'],
                        dados['registro'],
                        dados['salario']
                    )
                    secretarios[secretario.registro] = secretario
        except FileNotFoundError:
            self.data = []
        except json.JSONDecodeError:
            print("Erro ao carregar secretarios: arquivo JSON está malformado")
            self.data = []
        return secretarios

    def adicionar_secretario(self, secretario: Secretario):
        self.add_item(secretario.registro, {
            "nome": secretario.nome,
            "idade": secretario.idade,
            "email": secretario.email,
            "registro": secretario.registro,
            "salario": secretario.salario
        })
        self.secretarios = self.carregar_secretarios()

    def remover_secretario(self, registro):
        self.remove_item(registro)
        self.secretarios = self.carregar_secretarios()

    def buscar_secretario(self, registro):
        return self.secretarios.get(registro)

    def buscar_secretario_por_nome(self, nome):
        for secretario in self.secretarios.values():
            if secretario.nome == nome:
                return secretario
        return None