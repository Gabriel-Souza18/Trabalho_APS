from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula,notas, turma, email):
        super().__init__(nome, idade,email)
        self.matricula = matricula
        self.notas = notas
        self.turma = turma

    def imprimir_aluno(self):
        print(f'Nome:{self.nome},Idade:{self.idade},Matricula: {self.matricula}, Turma:{self.turma}, Email: {self.email}')
    
    def mudar_nota(self, materia, nota):
        self.notas[materia] = nota