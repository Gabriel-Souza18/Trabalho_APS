from .Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, idade, email, matricula, turma, notas):
        super().__init__(nome, idade, email)
        self.matricula = matricula
        self.turma = turma
        self.notas = notas

    def __str__(self):
        return f"Aluno(nome={self.nome}, idade={self.idade}, email={self.email}, matricula={self.matricula}, turma={self.turma}, notas={self.notas})"

    __repr__ = __str__
