from .Materia import Materia

class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.alunos = []
        self.materias = []
