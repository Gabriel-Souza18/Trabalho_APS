import json
import pickle

import self
from persistencia import Escola
class Leitor():
    def __init__(self, escola: Escola):
        self.escola = escola

    def lista_secretarios(self, caminho):
        with open(caminho, "r") as arquivo:
            secretarios = json.load(arquivo)
            for secretario in secretarios:
                self.escola.add_secretario(secretario["nome"], secretario["idade"], secretario["email"],
                                           secretario["registro"], secretario["salario"])

    def lista_professores(self, caminho):
        with open(caminho, "r") as arquivo:
            professores = json.load(arquivo)
            for professor in professores:
                self.escola.add_professor(professor["nome"], professor["idade"], professor["email"],
                                          professor["registro"], professor["salario"])

    def lista_alunos(self, caminho):
        with open(caminho, "r") as arquivo:
            alunos = json.load(arquivo)
            for aluno in alunos:
                self.escola.add_aluno(aluno['nome'], aluno['idade'],aluno['email'],
                                      aluno['matricula'], aluno['turma'])

        for aluno in self.escola.Alunos.values():
            for turma in self.escola.Turmas:
                if aluno.turma == turma.nome_turma:
                    aluno.turma = turma
                    turma.alunos.append(alunos)







def parse_notas(notas_str):
    notas_list = notas_str.split(", ")  # Divide a string em uma lista de pares chave-valor
    notas_dict = {}
    for nota in notas_list:
        materia, valor = nota.split(": ")
        notas_dict[materia] = int(valor)
    return notas_dict