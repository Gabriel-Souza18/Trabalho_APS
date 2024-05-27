from pessoas import*
import PySimpleGUI as sg

class TelaLogin():
    def __init__(self):
        self.entrou = False
        self.tipoUsuario = None        
        sg.theme('DarkBlue12')

    def show_tela_login(self):
        layout = [
            [sg.Text("Registro"), sg.Input(key="REGISTRO")],
            [sg.Text("Senha"), sg.Input(key="SENHA")],
            [sg.Button("Entrar", key="ENTRAR")]
        ]

        window = sg.Window("Login", layout, size=(300,100))

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED : 
                break

            if event == "ENTRAR":
                registro = values["REGISTRO"]
                senha = values["SENHA"]
                if self.conferir_senha(registro,senha):
                    self.entrou = True
                    break
                else:
                    sg.popup("Senha errada")
            ''' 
            if event == "CADASTRAR":
                registro = values["REGISTRO"]
                senha = values["SENHA"]
                self.cadastrar_usuario(registro, senha)
            '''
                
    def conferir_senha(self, registro, senha):
        with open('senhas.txt', 'r') as arquivo:
            for linha in arquivo:
                tipo, reg, sen = linha.strip().split(',')
                if reg == registro and sen == senha:
                    self.tipoUsuario = tipo
                    return True
            return False
    '''   
    def cadastrar_usuario(self, usuario, senha):
        tipo_usuario = usuario.__class__.__name__
        registro = usuario.matricula if tipo_usuario == Aluno else usuario.registro
        with open('senhas.txt', 'a') as arquivo:
            arquivo.write(f'{tipo_usuario},{registro},{senha}\n')
    '''
