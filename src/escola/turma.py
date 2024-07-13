from .materia import Materia
from src.pessoas import Aluno, Professor


class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.alunos = {}
        self.materias = {}

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos[aluno.nome] = aluno

    def adicionar_materia(self, materia: Materia):
        self.materias[materia.nome] = materia
        self.materias[materia.nome].adicionar_turma(self)
        materia.professor = self

    def retornar_materia(self, nome_materia):
        for materia in self.materias:
            if materia.nome == nome_materia:
                return materia
        return None

    def imprimir_turma(self):
        for materia in self.materias:
            print(f'Professor: {materia.professor.nome} de {materia.nome}')

        for _, aluno in self.alunos.items():
            print(f'Aluno {aluno.nome}, Matricula: {aluno.matricula}, Materias:{list(aluno.notas)} ')
