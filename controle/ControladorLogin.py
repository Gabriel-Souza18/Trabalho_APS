import PySimpleGUI as sg

from persistencia.RegistroDAO import RegistroDAO
from persistencia.AlunoDAO import AlunoDAO
from persistencia.TurmaDAO import TurmaDAO
from persistencia.ProfessorDAO import ProfessorDAO
from persistencia.SecretarioDAO import SecretarioDAO
from persistencia.MateriaDAO import MateriaDAO

from visao.telaLogin import tela_login_layout
from visao.telaInicialAluno import layout_tela_inicial_aluno
from visao.telaInicialSecretario import telaInicialSecretario
from visao.telaInicialProfessor import TelaInicialProfessor

from controle.ControladorAluno import ControladorTelaInicialAluno

class ControladorLogin:
    def __init__(self):
        # Inicializa os DAOs básicos
        self.registro_dao = RegistroDAO()
        self.aluno_dao = AlunoDAO()
        self.professor_dao = ProfessorDAO()
        self.secretario_dao = SecretarioDAO()
        self.turma_dao = TurmaDAO(self.aluno_dao)  # Passa o aluno_dao
        self.materia_dao = MateriaDAO(self.professor_dao)

        # Atualiza MateriaDAO com a instância correta de TurmaDAO
        self.turma_dao.materia_dao = self.materia_dao
        self.materia_dao.turma_dao = self.turma_dao

    def iniciar_tela_login(self):
        window = tela_login_layout()

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Sair':
                break

            if event == 'Entrar':
                registro = values['REGISTRO']
                senha = values['SENHA']
                
                tipo_usuario = self.registro_dao.get_tipo(registro)
                
                if tipo_usuario and self.registro_dao.testar_senha(registro, senha):
                    if tipo_usuario == 'A':
                        aluno = self.aluno_dao.buscar_aluno(registro)
                        if aluno:
                            turma = self.turma_dao.buscar_turma(aluno.turma)
                            if turma:
                                controlador_aluno = ControladorTelaInicialAluno(self.aluno_dao, self.turma_dao, self.materia_dao)
                                controlador_aluno.iniciar_tela_inicial_aluno(aluno, turma)
                            else:
                                sg.popup('Turma não encontrada!', title="Erro", font=("Arial", 14))
                        else:
                            sg.popup('Aluno não encontrado!', title="Erro", font=("Arial", 14))

                    elif tipo_usuario == 'P':
                        professor = self.professor_dao.buscar_professor(registro)
                        if professor:
                            TelaInicialProfessor(professor, self.professor_dao)
                        else:
                            sg.popup('Professor não encontrado!', title="Erro", font=("Arial", 14))

                    elif tipo_usuario == 'S':
                        secretario = self.secretario_dao.buscar_secretario(registro)
                        if secretario:
                            telaInicialSecretario(secretario, self.secretario_dao)
                        else:
                            sg.popup('Secretário não encontrado!', title="Erro", font=("Arial", 14))

                    else:
                        sg.popup('Tipo de usuário desconhecido!', title="Erro", font=("Arial", 14))

                else:
                    sg.popup('Usuário ou senha incorretos!', title="Erro", font=("Arial", 14))

        window.close()
