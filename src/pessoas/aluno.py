from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula,notas, turma):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = notas
        self.turma = turma

    def imprimir_aluno(self):
        print(f'Nome:{self.nome},Idade:{self.idade},Matricula: {self.matricula}, Turma:{self.turma}')
    
    def mudar_nota(self, materia, nota):
        self.notas[materia] = nota