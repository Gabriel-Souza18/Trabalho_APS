import PySimpleGUI as sg
from pessoas import *
from escola import*

def TelaInicial(aluno, turma):
    sg.theme('DarkBlue12')
    

    layout=[
[sg.Text('Nome: '+aluno.nome, font=("Arial 14")), sg.Text('', size=(15,1)), sg.Text(f'Matricula: '+aluno.matricula, font=("Arial 14"))],        [sg.Button("Ver Notas", key = "NOTAS", size=(25,20)),sg.Button("Ver Turma", key = "TURMA",size=(25,20))]
    ]
    window = sg.Window("Aluno",layout, size=(450,100))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED : 
            break

        if event == "NOTAS":
            tela_notas(aluno)


        if event == "TURMA":
            tela_turma(turma)
    window.close()

def tela_notas(aluno):    
    layout=[[sg.Multiline(key='-ML-', write_only=True, size=(60,10))],
            [[sg.Button('FECHAR')]]
        ]
    
    window = sg.Window('Notas',layout,finalize=True)
    
    for materia, nota in aluno.notas.items():
        window['-ML-'].print(f'Materia: {materia}, Nota: {nota}')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "FECHAR": 
            break
    window.close()

    
def tela_turma(turma):
    layout=[[sg.Multiline(key='-ML-', write_only=True, size=(60,10))],
            [[sg.Button('FECHAR')]]
        ]
    
    window = sg.Window("Turma",layout,finalize=True)
    
    for _, aluno in turma.alunos.items():
        window['-ML-'].print(f'{aluno.nome}: Idade: {aluno.idade}, Matricula: {aluno.matricula}')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "FECHAR" : 
            break
    window.close()



diretor =Diretor("Diretor",50,'3216516')
Turma1 = diretor.ler_turma("Turma1")
diretor.adicionar_turma(Turma1)

aluno = Turma1.alunos["Joao"]

TelaInicial(aluno, Turma1)
