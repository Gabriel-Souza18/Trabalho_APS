from .Materia import Materia

class Turma:
    def __init__(self, nomeTurma):
        self.nome_turma = nomeTurma
        self.alunos = []
        self.materias = []
