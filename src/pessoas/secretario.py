from src.escola.escola import Escola
from src.escola.turma import Turma

from src.pessoas.aluno import Aluno
from src.pessoas.pessoa import Pessoa


class Secretario(Pessoa):
    def __init__(self, nome, idade, registro, email, escola: Escola):
        super().__init__(nome, idade, email)
        self.registro = registro
        self.escola = escola

    def adicionar_turma(self, turma):
        self.escola.adicionar_turma(turma)

    def ler_turma(self, nome_turma):
        turma = Turma(nome_turma)
        with open(f"{nome_turma}.txt", "r") as arq:
            for linha in arq:
                nome, idade, matricula, notas, sala, email = linha.strip().split('/ ')
                # Convertendo a string de notas de volta para um dicionário
                notas = eval(notas)
                aluno = Aluno(nome, int(idade), matricula, notas, sala, email)
                turma.adicionar_aluno(aluno)
            arq.close()
            self.escola.adicionar_turma(turma)
        return 0

    def escrever_turma(self, nome_turma):
        with open(f"src/{nome_turma}.txt", 'w') as arq:
            for turma in self.escola.turmas:
                if turma.sala == nome_turma:
                    for aluno in turma.alunos:
                        arq.write(
                            f"{aluno.nome}/"
                            f" {aluno.idade}/ "
                            f"{aluno.matricula}/"
                            f" {dict(aluno.nota)}/"
                            f" {turma.sala}/"
                            f" {aluno.email}\n")
