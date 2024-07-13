from src.pessoas import Professor
from src.escola import Avaliacao


class Materia:
    def __init__(self, nome, professor: Professor):
        self.nome = nome
        self.professor = professor
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao: Avaliacao):
        self.avaliacoes.append(avaliacao)
