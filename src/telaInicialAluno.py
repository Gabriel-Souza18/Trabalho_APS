
import PySimpleGUI as sg
from pessoas import *
from escola import*

def TelaInicial(aluno, turma):
    sg.theme('DarkBlue12')
    
    layout=[
        [sg.Text('Nome: '+aluno.nome, font=("Arial 14")), sg.Text('', size=(15,1)), sg.Text(f'Matricula: '+aluno.matricula, font=("Arial 14"))],        
        [sg.Text(aluno.email, font=("Arial 14"))],
        [sg.Button("Ver Notas", key = "NOTAS", size=(25,20)),sg.Button("Ver Turma", key = "TURMA",size=(25,10))]
    ]
    window = sg.Window("Aluno",layout, size=(450,130))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED : 
            break

        if event == "NOTAS":
            tela_notas(aluno, turma)


        if event == "TURMA":
            tela_turma(turma)
    window.close()

def tela_notas(aluno, turma):
    layout = [[sg.Text("Clique na materia para ver detalhes", font=("Arial 14"))],
        [sg.Table(values=[],
                  
                  headings=["Matéria", "Nota"], 
                  key="Tabela", 
                  auto_size_columns= False,
                  max_col_width=17,
                  def_col_width=17,
                  justification='center',
                  enable_events = True)],
        [sg.Button('FECHAR')]
    ]
    
    window = sg.Window('Notas', layout, finalize=True, size=(350,250))

    linhas_tabela = []

    for materia, nota in aluno.notas.items():
        linhas_tabela.append([materia, nota])
        

    linhas_tabela.sort(key= lambda x: x[0])
        
    window['Tabela'].update(values=linhas_tabela)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'FECHAR':
            break

        elif event == 'Tabela':
            if values['Tabela']:
                linha_clicada = values['Tabela'][0]  # Obtém o índice da linha clicada
                nome_materia = linhas_tabela[linha_clicada][0]
                materia = turma.retornar_materia(nome_materia)
                if materia is not None:
                    tela_materia(materia)
                

    window.close()

    
def tela_turma(turma):
    layout = [
        [sg.Table(values=[],
                  headings=["Matrícula", "Nome", "Idade"], 
                  key="Tabela", 
                  auto_size_columns= False,
                  max_col_width=10,
                  def_col_width=10,
                  justification='center',
                  display_row_numbers=True,
                  starting_row_number=1)],
        [sg.Button('FECHAR')]
    ]
    
    window = sg.Window("Turma",layout,finalize=True, size=(350,200))

    linha_tabela = []
    
    for _, aluno in turma.alunos.items():
        linha_tabela.append([aluno.matricula, aluno.nome, aluno.idade])

    linha_tabela.sort(key= lambda x: x[1])

    window['Tabela'].update(values=linha_tabela)
    

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "FECHAR" : 
            break
    window.close()

def tela_materia(materia):
    dados_arvore = sg.TreeData()

    dados_arvore.insert("", "CP", "Provas", [('')])
    for prova, valor in materia.provas.items():
      dados_arvore.insert("CP", prova, prova, [(valor,)])

    dados_arvore.insert("", "CT", "Trabalhos", [('')])
    for trabalho, valor in materia.trabalhos.items():
        dados_arvore.insert("CT", trabalho, trabalho, [(valor,)])

    layout = [
        [sg.Text(f"{materia.nome} - Professor: {materia.professor}")],[
            sg.Tree(data=dados_arvore,
                 headings=["Valor"],
                 key="Arvore",
                 auto_size_columns=False,
                 max_col_width=22,
                 def_col_width=22,
                 justification='center')],
        [sg.Button('FECHAR')]
    ]

    window = sg.Window("Materia", layout, finalize=True, size=(350, 250))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "FECHAR":
            break
    window.close()

diretor =Diretor("Diretor", 50, '3216516',"diretor@hotmail.com")
Turma1 = diretor.ler_turma("Turma1")
diretor.adicionar_turma(Turma1)

matematica = Materia("Matematica", "Pedro")
matematica.adiconar_prova("Prova 1", 25)
matematica.adiconar_prova("Prova 2", 25)
matematica.adicionar_trabalho("TP 1", 15)
matematica.adicionar_trabalho("TP 2", 15)
matematica.adicionar_trabalho("TP 3", 15)
matematica.adicionar_trabalho("Listas", 5)

portugues = Materia("Portugues", "Carla")
portugues.adicionar_trabalho("Redação", 100)

Turma1.adicionar_materia(matematica)
Turma1.adicionar_materia(portugues)

aluno = Turma1.alunos["Joao"]

TelaInicial(aluno, Turma1)
