from modelo.pessoas.Secretario import Secretario
from modelo.pessoas.Professor import Professor
from modelo.pessoas.Aluno import Aluno
from modelo.escola.Materia import Materia
from modelo.escola.Turma import Turma
import random

class ControladorSecretario:
    def __init__(self, secretario_dao, aluno_dao, turma_dao, materia_dao, professor_dao, registro_dao):
        self.secretario_dao = secretario_dao
        self.aluno_dao = aluno_dao
        self.turma_dao = turma_dao
        self.materia_dao = materia_dao
        self.professor_dao = professor_dao
        self.registro_dao = registro_dao

    def obter_secretarios(self):
        return self.secretario_dao.buscar_secretarios()

    def adicionar_secretario(self, nome, idade, salario, email, registro):
        salario = float(salario)
        novo_secretario = Secretario(nome=nome, idade=idade, email=email, salario=salario, registro=registro)
        self.secretario_dao.adicionar_secretario(novo_secretario)
        self.criar_registro(registro, "S")

    def remover_secretario(self, registro):
        self.secretario_dao.remover_secretario(registro)
        self.secretario_dao.salvar_dados() 
        self.registro_dao.remover_registro(registro)
        self.registro_dao.salvar_registros()

    def adicionar_professor(self, nome, idade, email, salario, registro):
        professor = Professor(nome, idade, email, registro, salario)
        self.professor_dao.adicionar_professor(professor)
        self.criar_registro(registro, "P")

    def remover_professor(self, registro):
        self.professor_dao.remover_professor(registro)
        self.professor_dao.salvar_dados()
        self.registro_dao.remover_registro(registro)
        self.registro_dao.salvar_registros()

    def obter_professores(self):
        return self.professor_dao.buscar_professores()

    def obter_professor_por_nome(self, nome):
        return self.professor_dao.buscar_professor_por_nome(nome)

    def obter_professor(self, registro):
        return self.professor_dao.buscar_professor(registro)

    def obter_alunos(self):
        return self.aluno_dao.buscar_alunos()

    def adicionar_aluno(self, nome, idade, email, matricula, turma):
        novo_aluno = Aluno(nome=nome, idade=idade, email=email, matricula=matricula, turma=turma, notas={})
        self.aluno_dao.adicionar_aluno(novo_aluno)
        self.turma_dao.adicionar_aluno_em_turma(turma, matricula)
        self.criar_registro(matricula, "A")

    def remover_aluno(self, matricula):
        self.aluno_dao.remover_aluno(matricula)
        self.aluno_dao.salvar_dados()
        self.registro_dao.remover_registro(matricula)
        self.registro_dao.salvar_registros()
        self.turma_dao.remover_aluno_de_turma(matricula)

    def obter_turmas(self):
        return self.turma_dao.buscar_turmas()

    def obter_materias(self):
        return self.materia_dao.buscar_materias()

    def criar_registro(self, registro, tipo):
        senha = f"{random.randint(100, 999)}"
        self.registro_dao.adicionar_registro(registro, senha, tipo)
        print(f"Registro criado com sucesso! Registro: {registro}, Senha: {senha}, Tipo: {tipo}")

    def adicionar_materia(self, turma_nome, nome, professor):
        professor = self.professor_dao.buscar_professor_por_nome(professor)
        turma = self.turma_dao.buscar_turma(turma_nome)
        materia = Materia(nome, professor, turma, {}, {})
        self.materia_dao.adicionar_materia(materia)
        self.turma_dao.adicionar_materia_em_turma(turma_nome, materia.nome)

    def remover_materia(self, nome_materia):
        self.materia_dao.remover_materia(nome_materia)
        self.turma_dao.remover_turma_por_materia(nome_materia)

    def adicionar_turma(self, nome_turma):
        nova_turma = Turma(nome_turma, {}, {})
        self.turma_dao.adicionar_turma(nova_turma)
        print(f"Turma {nome_turma} adicionada com sucesso.")

    def remover_turma(self, nome_turma):
        turma = self.turma_dao.buscar_turma(nome_turma)
        if turma:
            self.turma_dao.remover_turma(nome_turma)
            print(f"Turma {nome_turma} removida com sucesso.")
        else:
            print(f"Turma {nome_turma} não encontrada.")
