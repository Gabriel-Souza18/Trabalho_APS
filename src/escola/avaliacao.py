from escola import *
from pessoas import *

class Avaliacao():
    def __init__(self,materia, data):
        self.materia = materia
        self.data = data
        self.notas = {}  


    def modificar_nota(self, aluno, nota):
        self.notas[aluno] = nota

    def imprimir_notas(self):
        for aluno, nota in self.notas.items():
            print(f'NOME: {aluno}, NOTA: {nota}')