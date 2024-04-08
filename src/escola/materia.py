
class Materia():
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.provas = {}
        self.trabalhos = {}

    def adiconar_prova(self, prova, valor):
        self.provas[prova] = valor
    
    def adicionar_trabalho(self, trabalho, valor):
        self.trabalhos[trabalho] = valor
        
