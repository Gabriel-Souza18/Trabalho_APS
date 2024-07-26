import PySimpleGUI as sg
from persistencia.Leitor import Leitor

def telaLogin():
    layout = [
        [sg.Text('Registro: ', font=("Arial 14"))],
        [sg.Input(key='REGISTRO', font=("Arial 14"))],
        [sg.Text('Senha: ', font=("Arial 14"))],
        [sg.Input(key='SENHA', password_char='*', font=("Arial 14"))],
        [sg.Button('Entrar', font=("Arial 14")), sg.Button('Sair', font=("Arial 14"))]
    ]

    window = sg.Window("Tela de Login", layout, size=(350, 180))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break

        if event == 'Entrar':
            registro = values['REGISTRO']
            senha = values['SENHA']
            
            Leitor.testar_senha(Leitor, registro, senha)

            resultado = Leitor.testar_senha(Leitor, registro, senha)

            if resultado!= 'N':
                if(resultado == 'A'):
                    print("Aluno")
                elif(resultado == 'P'):
                    print("Professor")
                else:
                    print("Secretario")

                # Tenta criar uma função no leitor que recebe o registro e retorna a Pessoa.
                # Ai pega os dados e abrimos o menu proprio daquela pessoa

                
            else:
                sg.popup('Usuário ou senha incorretos!', title="Erro", font=("Arial 14"))

    window.close()