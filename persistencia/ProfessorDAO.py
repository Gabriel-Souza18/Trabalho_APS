import json
from modelo.pessoas.Professor import Professor
from persistencia.BaseDAO import BaseDAO

CAMINHO = "persistencia/dados/"

class ProfessorDAO(BaseDAO):
    def __init__(self):
        self.professores = {}  # Dicionário para armazenar professores com o registro como chave
        self.carregar_professores()  # Carrega os professores no início

    def salvar_professores(self):
        """Salva todos os professores no arquivo JSON."""
        professores_data = [
            {
                "nome": professor.nome,
                "idade": professor.idade,
                "email": professor.email,
                "registro": professor.registro,
                "salario": professor.salario
            }
            for professor in self.professores.values()
        ]
        with open(CAMINHO + "professores.json", "w", encoding="utf-8") as arquivo:
            json.dump(professores_data, arquivo, indent=4, ensure_ascii=False)

    def carregar_professores(self):
        """Carrega os professores do arquivo JSON e os armazena no dicionário."""
        try:
            with open(CAMINHO + "professores.json", 'r', encoding='utf-8') as arquivo:
                professores_data = json.load(arquivo)
                for dados in professores_data:
                    professor = Professor(
                        dados['nome'],
                        dados['idade'],
                        dados['email'],
                        dados['registro'],
                        dados['salario']
                    )
                    self.professores[professor.registro] = professor
        except FileNotFoundError:
            # Caso o arquivo não exista, apenas ignore
            pass

    def adicionar_professor(self, professor: Professor):
        """Adiciona um professor ao dicionário e salva as alterações."""
        self.professores[professor.registro] = professor
        self.salvar_professores()

    def remover_professor(self, registro):
        """Remove um professor pelo registro e salva as alterações."""
        if registro in self.professores:
            del self.professores[registro]
            self.salvar_professores()

    def buscar_professor(self, registro):
        """Busca e retorna um professor pelo registro."""
        return self.professores.get(registro)

    def buscar_professor_por_nome(self, nome):
        """Busca e retorna um professor pelo nome."""
        for professor in self.professores.values():
            if professor.nome == nome:
                return professor
        return None
