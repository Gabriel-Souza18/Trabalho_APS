import json

from persistencia.BaseDAO import BaseDAO
from modelo.pessoas.Aluno import Aluno

class AlunoDAO(BaseDAO):
    def __init__(self):
        super().__init__("alunos.json")
        self.alunos = self.carregar_alunos()

    def carregar_alunos(self):
        alunos = {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as arquivo:
                self.data = json.load(arquivo)
                for dados in self.data:
                    aluno = Aluno(
                        dados['nome'],
                        dados['idade'],
                        dados['email'],
                        dados['matricula'],
                        dados['turma'],
                        dados['notas']
                    )
                    alunos[aluno.matricula] = aluno
        except FileNotFoundError:
            self.data = []
        except json.JSONDecodeError:
            print("Erro ao carregar alunos: arquivo JSON está malformado")
            self.data = []
        return alunos

    def adicionar_aluno(self, aluno: Aluno):
        self.add_item(aluno.matricula, {
            "nome": aluno.nome,
            "idade": aluno.idade,
            "email": aluno.email,
            "turma": aluno.turma,
            "notas": aluno.notas
        })
        self.alunos = self.carregar_alunos()

    def remover_aluno(self, matricula):
        self.remove_item(matricula)
        self.alunos = self.carregar_alunos()

    def buscar_aluno(self, matricula):
        return self.alunos.get(matricula)