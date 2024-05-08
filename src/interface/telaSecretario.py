import PySimpleGUI as sg

from pessoas import *
from escola import *

class TelaSecretario():  
    def show_tela_secretario(self):
        layout =[
            [sg.Button("Adicionar Aluno", key = "ADD_ALUNO"), 
                sg.Button("Adicionar Professor", key= "ADD_PROFESSOR")],
            [sg.Button("Listar turma", key= "LIST_TURMA"),
                sg.Button("Listar professores", key="LIST_PROFESSOR")],
            []
        ]
        window = sg.Window("Secretario", layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED : 
                break
            if event == "ADD_ALUNO":
                print(f"adicionar aluno")
            if event == "ADD_PROFESSOR":
                print(f"adicionar PROFESSOR")
            if event == "LIST_TURMA":
                print(f"listar turma")
            if event == "LIST_PROFESSOR":
                print(f"listar professor")        
            