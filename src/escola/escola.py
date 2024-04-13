from pessoas import *
from .materia import Materia
from .turma import Turma

class Escola():
    def __init__(self):
        self.secretarios = {}
        self.professores = {}
        self.turmas = {}

    def adicionar_secretario(self,secretario):
        self.secretarios[secretario.nome] = secretario

    def adicionar_professor(self, professor):
        self.professores[professor.nome] = professor

    def adicionar_turma(self, turma):
        self.turmas[turma.nome_turma] = turma


        