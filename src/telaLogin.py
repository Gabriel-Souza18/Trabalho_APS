from pessoas import*
import PySimpleGUI as sg

def tela_login():
    sg.theme('DarkBlue12')
    layout = [
        [sg.Text("Registro"), sg.Input(key="REGISTRO")],
        [sg.Text("Senha"), sg.Input(key="SENHA")],
        [sg.Button("Entrar", key="ENTRAR"),sg.Button("Cadastrar", key= "CADASTRAR")]
    ]

    window = sg.Window("Login", layout, size=(300,100))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED : 
            break

        if event == "ENTRAR":
            registro = values["REGISTRO"]
            senha = values["SENHA"]
            if conferir_senha(registro,senha):
                sg.popup("Entrou")
            else:
                sg.popup("Senha errada")
        
        if event == "CADASTRAR":
            registro = values["REGISTRO"]
            senha = values["SENHA"]
            cadastrar_usuario(registro, senha)

def conferir_senha(registro, senha):
    with open('senhas.txt', 'r') as arquivo:
        for linha in arquivo:
            reg, sen = linha.strip().split(',')
            if reg == registro and sen == senha:
                return True
        return False
    
def cadastrar_usuario(registro, senha):
    with open('senhas.txt', 'a') as arquivo:
        arquivo.write(f'{registro},{senha}\n')
    print("Usuário cadastrado com sucesso!")

tela_login()