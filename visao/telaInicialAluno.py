import PySimpleGUI as sg

def TelaInicial(aluno, turma, escola):
    sg.theme('DarkBlue12')

    layout = [
        [sg.Text('Nome: ' + aluno.nome, font=("Arial", 14)), sg.Text('', size=(15, 1)), sg.Text(f'Matricula: ' + str(aluno.matricula), font=("Arial", 14))],
        [sg.Text(aluno.email, font=("Arial", 14))],
        [sg.Button("Ver Notas", key="NOTAS", size=(15, 1), font=("Arial", 14)), sg.Button("Ver Turma", key="TURMA", size=(15, 1), font=("Arial", 14))]
    ]
    window = sg.Window("Aluno", layout, size=(450, 150), element_justification='center', finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == "NOTAS":
            window.close()
            tela_notas(aluno, turma, escola)

        if event == "TURMA":
            window.close()
            tela_turma(turma)
    window.close()

def tela_notas(aluno, turma, escola):
    layout = [
        [sg.Text("Clique na matéria para ver detalhes", font=("Arial", 14), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[],
                  headings=["Matéria", "Nota"],
                  key="Tabela",
                  auto_size_columns=False,
                  col_widths=[20, 10],
                  justification='center',
                  enable_events=True,
                  font=("Arial", 14),
                  row_height=25)],
        [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))), sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window('Notas', layout, finalize=True, size=(450, 400), element_justification='center')

    linhas_tabela = []

    for materia, nota in aluno.notas.items():
        linhas_tabela.append([materia, nota])

    linhas_tabela.sort(key=lambda x: x[0])

    window['Tabela'].update(values=linhas_tabela)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Fechar':
            break

        elif event == 'Voltar':
            window.close()
            return  # Retorna para a tela anterior

        elif event == 'Tabela':
            if values['Tabela']:
                linha_clicada = values['Tabela'][0]  # Obtém o índice da linha clicada

                nome_materia = linhas_tabela[linha_clicada][0]
                materia = escola.get_materia_por_nome(nome_materia)
                tela_materia(materia)

    window.close()

def tela_turma(turma):
    layout = [
        [sg.Text(f"Turma: {turma.nome_turma}", font=("Arial", 14), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[],
                  headings=["Matrícula", "Nome", "Idade"],
                  key="Tabela",
                  auto_size_columns=False,
                  col_widths=[10, 20, 10],
                  justification='center',
                  display_row_numbers=True,
                  font=("Arial", 14),
                  row_height=25)],
        [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))), sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window("Turma", layout, finalize=True, size=(450, 400), element_justification='center')

    linha_tabela = []

    for aluno in turma.alunos:
        linha_tabela.append([aluno.matricula, aluno.nome, aluno.idade])

    linha_tabela.sort(key=lambda x: x[1])

    window['Tabela'].update(values=linha_tabela)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Fechar":
            break

        elif event == 'Voltar':
            window.close()
            return  # Retorna para a tela anterior

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
        [sg.Text(f"{materia.nome} - Professor: {materia.professor.nome}", font=("Arial", 14), pad=((0, 0), (10, 10)))],
        [sg.Tree(data=dados_arvore,
                 headings=["Valor"],
                 key="Arvore",
                 auto_size_columns=False,
                 col_widths=[30],
                 justification='center',
                 font=("Arial", 14),
                 row_height=25)],
        [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))), sg.Button('FECHAR', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window("Materia", layout, finalize=True, size=(450, 300), element_justification='center')

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "FECHAR":
            break

        elif event == 'Voltar':
            window.close()
            return  # Retorna para a tela anterior

    window.close()

