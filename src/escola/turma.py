from .materia import Materia

import sys
sys.path.append('src')
from pessoas import*


class Turma():
    def __init__(self,nome_turma):
        self.nome_turma = nome_turma
        self.alunos = {}
        self.materias = []
        self.sala = None

    def adicionar_aluno(self, aluno):
        self.alunos[aluno.nome] = aluno

    def adicionar_materia(self, materia):
        self.materias.append(materia)

    def retornar_materia(self, nome_materia):
        for materia in self.materias:
            if materia.nome == nome_materia:
                return materia
        return None

    def imprimir_turma(self):
        for materia in self.materias:
            print(f'Professor: {materia.professor.nome} de {materia.nome}')
        
        for _, aluno in self.alunos.items():
            print(f'Aluno {aluno.nome}, Matricula: {aluno.matricula}, Notas:{dict(aluno.notas)} ')
        
