from ..pessoas.Professor import Professor

class Materia:
    def __init__(self, nome, Profesor):
        self.nome = nome
        self.Professor = Profesor
        self.provas = {}
        self.trabalhos = {}
        
        