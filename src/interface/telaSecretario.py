import PySimpleGUI as sg

from src.pessoas.secretario import *
from src.escola.escola import *

class TelaSecretario():
    def __init__(self,escola: Escola, registro):
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
                self.show_tela_novo_professor()
            if event == "LIST_TURMA":
                print(f"listar turma")
                self.show_tela_lista_turmas()
            if event == "LIST_PROFESSOR":
                print(f"listar professor")
                self.show_tela_lista_professores()        
    
    
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
            if event == sg.WIN_CLOSED: 
                break
            if event == "CANCELAR":
                break
            
            if event == "CADASTRAR":
                novo_aluno = Aluno(values["NOME"],values["IDADE"], values["MATRICULA"], None, values["TURMA"], values["EMAIL"])
                self.escola.adicionar_aluno(novo_aluno)
                self.escola.cadastrar_usuario(novo_aluno, novo_aluno.matricula)
                
                Secretario.escrever_turma(nome_turma=novo_aluno.turma)
                break
           
    def show_tela_novo_professor(self):
        layout=[
            [sg.Text("Nome"), sg.Input(key= "NOME")],
            [sg.Text("Idade"), sg.Input(key = "IDADE")],
            [sg.Text("Registro"), sg.Input(key = "REGISTRO")],
            [sg.Text("Salario"), sg.Input(key = "SALARIO")],
            [sg.Text("Email"), sg.Input(key = "EMAIL")],
            [sg.Button("Cadastrar", key = "CADASTRAR"), sg.Button("Cancelar", key="CANCELAR")]
        ]
        window_novo_professor = sg.Window("Cadastar novo Professor", layout=layout)
        while True:
            event, values = window_novo_professor.read()
            if event == sg.WIN_CLOSED: 
                break
            if event == "CANCELAR":
                break
            
            if event == "CADASTRAR":
                novo_professor = Professor(values["NOME"],values["IDADE"],values["REGISTRO"],values["SALARIO"],values["EMAIL"])
                self.escola.adicionar_professor(novo_professor)
                self.escola.cadastrar_usuario(novo_professor, novo_professor.registro)
            
    def show_tela_lista_turmas():
        print("Lista de turmas")
    
    def show_tela_lista_professores():         
        print("Lista professores")