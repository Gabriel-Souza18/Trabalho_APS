
class Materia():
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.provas = []
        self.trabalhos = []

    def adiconar_prova(self, prova):
        self.provas.append(prova)
    
    def adicionar_trabalho(self, trabalho):
        self.trabalhos.append(trabalho)
        