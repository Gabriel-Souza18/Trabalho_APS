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
                if isinstance(self.data, list):
                    # Se self.data for uma lista, converte para um dicionário
                    for dados in self.data:
                        secretario = Secretario(
                            dados['nome'],
                            dados['idade'],
                            dados['email'],
                            dados['registro'],
                            dados['salario']
                        )
                        secretarios[secretario.registro] = secretario
                elif isinstance(self.data, dict):
                    # Se self.data já é um dicionário, carrega diretamente
                    for registro, dados in self.data.items():
                        secretario = Secretario(
                            dados['nome'],
                            dados['idade'],
                            dados['email'],
                            dados['registro'],
                            dados['salario']
                        )
                        secretarios[registro] = secretario
        except FileNotFoundError:
            self.data = {}
        except json.JSONDecodeError:
            print("Erro ao carregar secretários: arquivo JSON está malformado")
            self.data = {}
        return secretarios

    def salvar_dados(self):
        """Salva os dados no arquivo JSON no formato esperado."""
        dados_para_salvar = {reg: {
            "nome": sec.nome,
            "idade": sec.idade,
            "email": sec.email,
            "registro": sec.registro,
            "salario": sec.salario
        } for reg, sec in self.secretarios.items()}
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(dados_para_salvar, file, indent=4, ensure_ascii=False)

    def adicionar_secretario(self, secretario: Secretario):
        self.secretarios[secretario.registro] = secretario
        self.salvar_dados()  # Salvar alterações no arquivo JSON

    def remover_secretario(self, registro):
        if registro in self.secretarios:
            del self.secretarios[registro]
            self.salvar_dados()  # Salvar alterações no arquivo JSON

    def buscar_secretario(self, registro):
        return self.secretarios.get(registro)

    def buscar_secretarios(self):
        return self.secretarios.values()

    def buscar_secretario_por_nome(self, nome):
        for secretario in self.secretarios.values():
            if secretario.nome == nome:
                return secretario
        return None
