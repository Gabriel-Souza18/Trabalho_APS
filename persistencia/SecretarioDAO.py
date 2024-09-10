import json
from modelo.pessoas.Secretario import Secretario

CAMINHO = "persistencia/dados/"

class SecretarioDAO:
    def __init__(self):
        self.secretarios = {}  # Dicionário para armazenar secretários com o registro como chave
        self.carregar_secretarios()  # Carrega os secretários no início

    def salvar_secretarios(self):
        """Salva todos os secretários no arquivo JSON."""
        secretarios_data = [
            {
                "nome": secretario.nome,
                "idade": secretario.idade,
                "email": secretario.email,
                "registro": secretario.registro,
                "salario": secretario.salario
            }
            for secretario in self.secretarios.values()
        ]
        with open(CAMINHO + "secretarios.json", "w", encoding="utf-8") as arquivo:
            json.dump(secretarios_data, arquivo, indent=4, ensure_ascii=False)

    def carregar_secretarios(self):
        """Carrega os secretários do arquivo JSON e os armazena no dicionário."""
        try:
            with open(CAMINHO + "secretarios.json", 'r', encoding='utf-8') as arquivo:
                secretarios_data = json.load(arquivo)
                for dados in secretarios_data:
                    secretario = Secretario(
                        dados['nome'],
                        dados['idade'],
                        dados['email'],
                        dados['registro'],
                        dados['salario']
                    )
                    self.secretarios[secretario.registro] = secretario
        except FileNotFoundError:
            # Caso o arquivo não exista, apenas ignore
            pass

    def adicionar_secretario(self, secretario: Secretario):
        """Adiciona um secretário ao dicionário e salva as alterações."""
        self.secretarios[secretario.registro] = secretario
        self.salvar_secretarios()

    def remover_secretario(self, registro):
        """Remove um secretário pelo registro e salva as alterações."""
        if registro in self.secretarios:
            del self.secretarios[registro]
            self.salvar_secretarios()

    def buscar_secretario(self, registro):
        """Busca e retorna um secretário pelo registro."""
        return self.secretarios.get(registro)

    def buscar_secretario_por_nome(self, nome):
        """Busca e retorna um secretário pelo nome."""
        for secretario in self.secretarios.values():
            if secretario.nome == nome:
                return secretario
        return None
