from escola import *
from pessoas import *

class Materia():
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.avaliacoes = []
        self.turmas = []
        
    def adicionar_turma(self, turma):
        self.turmas.append(turma)

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)
    
    def imprimir_turmas(self):
        for turma in self.turmas:
            print(turma.nome_turma)

