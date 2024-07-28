from ..pessoas.Professor import Professor

class Materia:
    def __init__(self, nome, professor, turma):
        self.nome = nome
        self.professor = professor
        self.turma = turma
        self.provas = {}
        self.trabalhos = {}


