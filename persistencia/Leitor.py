
from persistencia import Escola

CAMINHO = "persistencia/dados/"

class Leitor():
    def __init__(self, escola: Escola):
        self.escola = escola

    def lista_secretarios(self): 
        with open(CAMINHO + "secretarios.txt", 'r') as arquivo:
            for linha in arquivo:
                nome, idade, email, registro, salario = linha.strip().split("/ ")
                self.escola.add_secretario(nome, idade, email, registro, salario)

    def lista_professores(self): #Funcionando
        with open(CAMINHO + "professores.txt", 'r') as arquivo:
            for linha in arquivo:
                nome, idade, email, registro, salario = linha.strip().split("/ ")
                self.escola.add_professor(nome, idade, email, registro, salario)


    def lista_alunos(self):
        with open(CAMINHO + "alunos.txt", 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split("/ ")
                nome = dados[0]
                idade = dados[1]
                matricula = dados[2]
                
                notas = {}
                i = 3
                while ":" in dados[i]:
                    disciplina, nota = dados[i].split(":")
                    notas[disciplina] = float(nota)
                    i += 1
                
                turma = dados[i]
                email = dados[i + 1]
                
                self.escola.add_aluno(nome, idade, email, matricula, turma, notas)

    def testar_senha(self, registro, senha):
        with open(CAMINHO + "registros.txt", 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(', ')
                if registro == partes[0] and senha == partes[1]:
                    return partes[2].strip().replace("'", "")
                
        return "N"
