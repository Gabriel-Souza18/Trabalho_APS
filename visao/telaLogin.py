import PySimpleGUI as sg
from persistencia.Leitor import Leitor
from controle.Escola import Escola

from visao.telaInicialAluno import *
from visao.telaInicialSecretario import *

def telaLogin(escola):
    sg.theme('DarkBlue12')  # Alterar tema para um tema mais moderno

    layout = [
        [sg.Text('Sistema Escolar', font=("Arial", 16), justification='center', pad=((0, 0), (10, 10)))],
        [sg.Text('Registro:', font=("Arial", 14), size=(10, 1)), sg.Input(key='REGISTRO', font=("Arial", 14), size=(20, 1), pad=((0, 0), (10, 10)))],
        [sg.Text('Senha:', font=("Arial", 14), size=(10, 1)), sg.Input(key='SENHA', password_char='*', font=("Arial", 14), size=(20, 1), pad=((0, 0), (10, 10)))],
        [sg.Button('Entrar', font=("Arial", 14), size=(10, 1), pad=((10, 0), (10, 10))), sg.Button('Sair', font=("Arial", 14), size=(10, 1), pad=((10, 0), (10, 10)))]
    ]

    window = sg.Window("Tela de Login", layout, size=(400, 250), element_justification='center')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break

        if event == 'Entrar':
            registro = values['REGISTRO']
            senha = values['SENHA']
            
            resultado = Leitor.testar_senha(Leitor, registro, senha)

            if resultado != 'N':
                if resultado == 'A':
                    aluno = escola.get_aluno(registro)
                    turma = escola.get_turma_do_aluno(aluno)

                    window.close()
                    TelaInicial(aluno, turma, escola)

                elif resultado == 'P':
                    professor = escola.get_professor(registro)
                    print(professor.nome)
                else:
                    secretario = escola.get_secretario(registro)
                    telaInicialSecretario(secretario, escola)


            else:
                sg.popup('Usuário ou senha incorretos!', title="Erro", font=("Arial", 14))

    window.close()

