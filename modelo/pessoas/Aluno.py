from .Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, email, matricula, turma, notas):
        super().__init__(nome, idade, email)
        self.matricula = matricula
        self.turma = turma
        self.notas = notas

    def imprimir(self):
        print(f"{self.nome} - {self.idade}: {self.email}, {self.matricula} ")
