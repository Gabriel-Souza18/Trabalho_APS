from .pessoa import Pessoa
import sys
sys.path.append('src')
from escola import *


class Professor(Pessoa):
    def __init__(self, nome, idade, registro, salario,email):
        super().__init__(nome, idade,email)
        self.registro = registro
        self.salario = salario
        self.materias = []
        self.turmas = []

    def adicionar_materia(self, materia):
        self.materias.append(materia)

    def adicionar_prova(self, avaliacao):
        for mat in self.materias:
            if mat.nome == avaliacao.materia.nome:
                mat.adicionar_avaliacao(avaliacao)
    
    '''
    def mudar_nota(self,nome_turma,nome_aluno, nota):
        for turma in self.turmas:
            if turma.sala == nome_turma:
                for aluno in turma.alunos:
                    if aluno.nome == nome_aluno:
                        aluno.nota = nota
                        return
        print("Turma ou aluno não encontrado")
    '''