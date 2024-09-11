import json

from persistencia.BaseDAO import BaseDAO
from modelo.escola.Turma import Turma


class TurmaDAO(BaseDAO):
    def __init__(self, aluno_dao):
        super().__init__("turmas.json")
        self.aluno_dao = aluno_dao
        self.turmas = self.carregar_turmas()

    def carregar_turmas(self):
        turmas = {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as arquivo:
                self.data = json.load(arquivo)
                for dados in self.data:
                    nome_turma = dados['nome']
                    alunos = [self.aluno_dao.buscar_aluno(matricula) for matricula in dados['alunos']]
                    turma = Turma(nome_turma)
                    turma.alunos = [aluno for aluno in alunos if aluno is not None]
                    turmas[nome_turma] = turma
        except FileNotFoundError:
            self.data = []
        except json.JSONDecodeError:
            print("Erro ao carregar turmas: arquivo JSON está malformado")
            self.data = []
        return turmas

    def adicionar_turma(self, turma):
        self.add_item(turma.nome_turma, {
            "alunos": [aluno.matricula for aluno in turma.alunos],
            "materias": [materia.nome for materia in turma.materias]
        })
        self.turmas = self.carregar_turmas()

    def remover_turma(self, nome_turma):
        self.remove_item(nome_turma)
        self.turmas = self.carregar_turmas()

    def buscar_turma(self, nome_turma):
        return self.turmas.get(nome_turma)
