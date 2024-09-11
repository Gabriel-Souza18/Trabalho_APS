import json
from modelo.pessoas.Professor import Professor
from persistencia.BaseDAO import BaseDAO


class ProfessorDAO(BaseDAO):
    def __init__(self):
        super().__init__("professores.json")
        self.professores = self.carregar_professores()

    def carregar_professores(self):
        professores = {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as arquivo:
                self.data = json.load(arquivo)
                for dados in self.data:
                    professor = Professor(
                        dados['nome'],
                        dados['idade'],
                        dados['email'],
                        dados['registro'],
                        dados['salario']
                    )
                    professores[professor.registro] = professor
        except FileNotFoundError:
            self.data = []
        except json.JSONDecodeError:
            print("Erro ao carregar professores: arquivo JSON está malformado")
            self.data = []
        return professores

    def adicionar_professor(self, professor: Professor):
        self.add_item(professor.registro, {
            "nome": professor.nome,
            "idade": professor.idade,
            "email": professor.email,
            "registro": professor.registro,
            "salario": professor.salario
        })
        self.professores = self.carregar_professores()

    def remover_professor(self, registro):
        self.remove_item(registro)
        self.professores = self.carregar_professores()

    def buscar_professor(self, registro):
        return self.professores.get(registro)

    def buscar_professor_por_nome(self, nome):
        for professor in self.professores.values():
            if professor.nome == nome:
                return professor
        return None
