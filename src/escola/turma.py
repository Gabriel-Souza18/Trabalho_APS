from pessoas import *
from .materia import Materia

class Turma():
    def __init__(self, sala):
        self.alunos = []
        self.materias = []
        self.sala = sala

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def adicionar_materia(self, materia):
        self.materias.append(materia)

    def imprimir_turma(self):
        for materia in self.materias:
            print(f'Professor: {materia.professor.nome} de `{materia.nome}')
        for aluno in self.alunos:
            print(f'Aluno {aluno.nome} matricula: {aluno.matricula}')

        