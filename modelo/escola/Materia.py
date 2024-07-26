from ..pessoas.Professor import Professor

class Materia:
    def __init__(self, nome, Professor):
        self.nome = nome
        self.Professor = Professor
        self.provas = {}
        self.trabalhos = {}
        
