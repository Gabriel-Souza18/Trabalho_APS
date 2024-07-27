from ..pessoas import Aluno
from ..pessoas.Professor import Professor

class Materia:
    def __init__(self, nome, professor: Professor):
        self.nome = nome
        self.professor = professor
        self.notas = {}
        self.provas = {}
        self.trabalhos = {}

    def adicionar_nota(self, aluno: Aluno, nota: int):
        self.notas[aluno.nome] = nota
