from src.pessoas import Aluno, Professor, Secretario
from src.escola import Escola, Turma


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.secretarios = {}
        self.professores = {}
        self.turmas = {}

    def adicionar_secretario(self, secretario:Secretario):  # Tem que passar a classse secretario e ta passsando uma str
        self.secretarios[secretario.nome] = secretario

    def adicionar_professor(self, professor:Professor):
        self.professores[professor.nome] = professor

    def adicionar_aluno(self, aluno: Aluno):
        self.turmas[aluno.turma].adicionar_aluno(aluno)  # ta dando erro aqui quando cadastro

    def adicionar_turma(self, turma: Turma):
        self.turmas[turma.nome_turma] = turma

    def buscar_secretario(self, registro):
        for secretario in self.secretarios:
            if secretario.registro == registro:
                return secretario
        return False

    def buscar_professor(self, registro):
        for professor in self.professores:
            if professor.registro == registro:
                return professor
        return False

    def cadastrar_usuario(self, usuario, senha):
        tipo_usuario = usuario.__class__.__name__
        if tipo_usuario == "Aluno":
            registro = usuario.matricula
        else:
            registro = usuario.registro
        with open('senhas.txt', 'a') as arquivo:
            arquivo.write(f'{tipo_usuario},{registro},{senha}\n')
