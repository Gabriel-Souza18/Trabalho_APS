import PySimpleGUI as sg

from pessoas import *
from escola import *

class TelaSecretario():
    def __init__(self,escola, registro):
        self.secretario = escola.buscar_secretario(registro)
        self.escola = escola  
      
    def show_tela_secretario(self):
        layout =[
            [sg.Button("Adicionar Aluno", key = "ADD_ALUNO"), 
                sg.Button("Adicionar Professor", key= "ADD_PROFESSOR")],
            [sg.Button("Listar turma", key= "LIST_TURMA"),
                sg.Button("Listar professores", key="LIST_PROFESSOR")],
            []
        ]
        window_secretario = sg.Window("Secretario", layout)

        while True:
            event, values = window_secretario.read()
            if event == sg.WIN_CLOSED : 
                break
            if event == "ADD_ALUNO":
                print(f"adicionar aluno")
                self.show_tela_novo_aluno()
            if event == "ADD_PROFESSOR":
                print(f"adicionar PROFESSOR")
            if event == "LIST_TURMA":
                print(f"listar turma")
            if event == "LIST_PROFESSOR":
                print(f"listar professor")        
    
    
    def show_tela_novo_aluno(self):
        layout =[
            [sg.Text("Nome"), sg.Input(key= "NOME")],
            [sg.Text("Idade"), sg.Input(key = "IDADE")],
            [sg.Text("Matricula"), sg.Input(key = "MATRICULA")],
            [sg.Text("Turma"), sg.Input(key = "TURMA")],
            [sg.Text("Email"), sg.Input(key = "EMAIL")],
            [sg.Button("Cadastrar", key = "CADASTRAR"), sg.Button("Cancelar", key="CANCELAR")]
        ]
        window_novo_aluno = sg.Window("Cadastro Novo aluno", layout=layout)
        while True:
            event, values = window_novo_aluno.read()
            if (event == sg.WIN_CLOSED) or (event == "CANCELAR") : 
                break
            if event == "CADASTRAR":
                novo_aluno = Aluno(values["NOME"],values["IDADE"], values["MATRICULA"], None, values["TURMA"], values["EMAIL"])
                self.escola.adicionar_aluno(novo_aluno)
                self.escola.cadastrar_usuario(novo_aluno, values["MATRICULA"])
                break
            