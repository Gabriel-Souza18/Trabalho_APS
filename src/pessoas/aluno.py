from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, nota, turma):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.nota = nota
        self.turma = turma

    def imprimir_aluno(self):
        print(f'Nome:{self.nome},Idade:{self.idade},Matricula: {self.matricula},Nota{self.nota}, Turma:{self.turma}')
    