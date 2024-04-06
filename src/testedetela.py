import PySimpleGUI as sg

from pessoas import *

def main():
    layout = [  [sg.Text('Criar aluno')],
                [sg.Text('Nome'), sg.InputText(key="NOME")],
                [sg.Text('Idade'), sg.InputText(key="IDADE")],
                [sg.Text('Matricula'), sg.InputText(key="MATRICULA")],
                [sg.Text('Turma'), sg.InputText(key="TURMA")],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # criar a tela
    window = sg.Window('Novo aluno', layout)

    # processar os eventos
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        novo_aluno = Aluno(values["NOME"], values["IDADE"],values["MATRICULA"],0,values["TURMA"])

        novo_aluno.imprimir_aluno()
    window.close()

main()

