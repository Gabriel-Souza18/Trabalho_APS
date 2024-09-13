import PySimpleGUI as sg

from persistencia.RegistroDAO import RegistroDAO
from persistencia.AlunoDAO import AlunoDAO
from persistencia.TurmaDAO import TurmaDAO
from persistencia.ProfessorDAO import ProfessorDAO
from persistencia.SecretarioDAO import SecretarioDAO
from persistencia.MateriaDAO import MateriaDAO

from controle.controlador_Aluno import ControladorAluno
from controle.controlador_Professor import ControladorProfessor
from controle.controlador_Secretario import ControladorSecretario

# Importa o layout da tela e passa o controlador para ele
from visao.tela_Login import tela_login_layout
from visao.tela_Aluno import TelaAluno
from visao.tela_Professor import TelaProfessor
from visao.tela_Secretario import TelaSecretario

class Controlador_Login:
    def __init__(self):
        self.registro_dao = RegistroDAO()
        self.aluno_dao = AlunoDAO()
        self.professor_dao = ProfessorDAO()
        self.secretario_dao = SecretarioDAO()
        self.turma_dao = TurmaDAO(self.aluno_dao)
        self.materia_dao = MateriaDAO(self.professor_dao, self.turma_dao)

    def iniciar(self):
        tela_login_layout(self)

    def processar_login(self, registro, senha):
        """Processa a tentativa de login do usuário."""
        if not self.validar_entrada(registro, senha):
            sg.popup('Usuário ou senha não podem estar vazios!', title="Erro", font=("Arial", 14))
            return

        tipo_usuario = self.registro_dao.get_tipo(registro)

        if not tipo_usuario:
            sg.popup('Usuário não encontrado!', title="Erro", font=("Arial", 14))
            return

        if not self.autenticar_usuario(registro, senha):
            sg.popup('Usuário ou senha incorretos!', title="Erro", font=("Arial", 14))
            return

        self.iniciar_interface_usuario(tipo_usuario, registro)

    def validar_entrada(self, registro, senha):
        """Valida se os campos de registro e senha não estão vazios."""
        return bool(registro and senha)

    def autenticar_usuario(self, registro, senha):
        """Testa se a senha do usuário está correta."""
        return self.registro_dao.testar_senha(registro, senha)

    def iniciar_interface_usuario(self, tipo_usuario, registro):
        """Inicia a interface de acordo com o tipo de usuário."""
        if tipo_usuario == 'A':
            self.iniciar_tela_aluno(registro)
        elif tipo_usuario == 'P':
            self.iniciar_tela_professor(registro)
        elif tipo_usuario == 'S':
            self.iniciar_tela_secretario(registro)
        else:
            sg.popup('Tipo de usuário desconhecido!', title="Erro", font=("Arial", 14))

    def iniciar_tela_aluno(self, registro):
        """Inicia a tela inicial para o aluno."""
        aluno = self.aluno_dao.buscar_aluno(registro)
        if not aluno:
            sg.popup('Aluno não encontrado!', title="Erro", font=("Arial", 14))
            return

        turma = self.turma_dao.buscar_turma(aluno.turma)
        if not turma:
            sg.popup('Turma não encontrada!', title="Erro", font=("Arial", 14))
            return

        controlador_aluno = ControladorAluno(self.aluno_dao, self.turma_dao, self.materia_dao)
        tela_aluno = TelaAluno(controlador_aluno)
        tela_aluno.tela_aluno(aluno, turma)

    def iniciar_tela_professor(self, registro):
        """Inicia a tela inicial para o professor."""
        professor = self.professor_dao.buscar_professor(registro)
        if not professor:
            sg.popup('Professor não encontrado!', title="Erro", font=("Arial", 14))
            return

        controlador_professor = ControladorProfessor(self.professor_dao, self.aluno_dao, self.turma_dao, self.materia_dao)
        tela_professor = TelaProfessor(controlador_professor)
        tela_professor.tela_professor(professor)

    def iniciar_tela_secretario(self, registro):
        """Inicia a tela inicial para o secretário."""
        secretario = self.secretario_dao.buscar_secretario(registro)
        if not secretario:
            sg.popup('Secretário não encontrado!', title="Erro", font=("Arial", 14))
            return

        controlador_secretatio = ControladorSecretario(self.secretario_dao, self.aluno_dao, self.turma_dao, self.materia_dao, self.professor_dao, self.registro_dao)
        tela_secretario = TelaSecretario(controlador_secretatio)
        tela_secretario.tela_inicial(secretario)
