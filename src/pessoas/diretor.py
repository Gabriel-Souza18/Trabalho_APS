from .professor import Professor
from .pessoa import Pessoa
from .aluno import Aluno
from escola import *

class Diretor(Pessoa):
    def __init__(self, nome, idade, registro):
        super().__init__(nome, idade)
        self.registro = registro
        self.professores = {}
        self.turmas = []

    def adicionar_turma(self, turma):
        self.turmas.append(turma)

    def ler_turma(self, nome_turma, sala):
        nova_turma = Turma(sala)
        with open(f"{nome_turma}.txt", "r") as arq:
            for linha in arq:
                nome, idade, matricula, nota, turma = linha.strip().split(', ')
                aluno = Aluno(nome, idade, matricula, nota, turma)
                nova_turma.adicionar_aluno(aluno)
        self.turmas.append(nova_turma)

    def escrever_turma(self, nome_turma):
        with open(f"{nome_turma}.txt", 'w') as arq:
            for turma in self.turmas:
                if turma.sala == nome_turma:
                    for aluno in turma.alunos:
                        arq.write(f"{aluno.nome}, {aluno.idade}, {aluno.matricula}, {aluno.nota}, {turma.sala}\n")


    
