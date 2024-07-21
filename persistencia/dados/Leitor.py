import self
from persistencia.dados import Escola
class Leitor():
    def __init__(self, caminho, escola: Escola):
        self.caminho = caminho
        self.escola = escola

    def lista_secretarios(self,arquivo):
        for secretario in arquivo:
            nome, idade, email, registro, salario = secretario.read().strip().split("/ ")
            self.escola.add_secretario(nome, idade, email, registro, salario)

    def lista_professores(self, arquivo):
        for professor in arquivo:
            nome, idade, email, registro, salario = professor.read().strip().split("/ ")
            self.escola.add_professor(nome, idade, email, registro, salario)

    def lista_alunos(self,arquivo):
        for aluno in arquivo:
            nome, idade, email, matricula, turma, notas = aluno.read().strip().split("/ ")
            self.escola.add_aluno(nome, idade, email, matricula, turma, notas)
