import PySimpleGUI as sg

def tela_login_layout(controlador):
    sg.theme('DarkBlue12')

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
            registro = values.get('REGISTRO', '')
            senha = values.get('SENHA', '')

            controlador.processar_login(registro, senha)

    window.close()
