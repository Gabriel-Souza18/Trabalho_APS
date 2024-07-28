import PySimpleGUI as sg

def telaInicialSecretario(secretario, escola):
    sg.theme('DarkBlue12')

    layout = [
        [sg.Text('Nome: ' + secretario.nome, font=("Arial", 14)),
         sg.Text('', size=(15, 1)),
         sg.Text(f'Matrícula: ' + str(secretario.registro), font=("Arial", 14))],
        [sg.Text(secretario.email, font=("Arial", 14))],
        [sg.Button("Ver Alunos", key="ALUNOS", size=(15, 1), font=("Arial", 14)),
         sg.Button("Ver Professores", key="PROFESSORES", size=(15, 1), font=("Arial", 14))],
        [sg.Button("Ver Turmas", key="TURMAS", size=(15, 1), font=("Arial", 14)),
         sg.Button("Ver Matérias", key="MATERIAS", size=(15, 1), font=("Arial", 14))]
    ]

    window = sg.Window("Secretário", layout, size=(450, 200), element_justification='center', finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            return 0

        if event == "ALUNOS":
            if tela_alunos(escola) == 0:
                window.close()
                return 0

        if event == "PROFESSORES":
            if tela_professores(escola) == 0:
                window.close()
                return 0

        if event == "TURMAS":
            if tela_turmas(escola) == 0:
                window.close()
                return 0

        if event == "MATERIAS":
            if tela_materias(escola) == 0:
                window.close()
                return 0

    window.close()
    return 0

def tela_materias(escola):
    materias = escola.Materias.values()
    layout = [
        [sg.Text("Lista de Matérias", font=("Arial", 14), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[[materia.nome, materia.professor.nome, materia.turma] for materia in materias],
                  headings=["Nome", "Professor", "Turma"],
                  key="Tabela",
                  auto_size_columns=False,
                  justification='center',
                  font=("Arial", 14),
                  row_height=25)],
        [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window("Matérias", layout, finalize=True, size=(450, 400), element_justification='center')

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Fechar":
            window.close()
            return 0
        elif event == 'Voltar':
            window.close()
            return 1

    window.close()
    return 0


def tela_adicionar_aluno(escola):
    novo_aluno_layout = [
        [sg.Text("Nome do Aluno:", size=(15, 1)), sg.InputText(key='nome')],
        [sg.Text("Idade do Aluno:", size=(15, 1)), sg.InputText(key='idade')],
        [sg.Text("Matrícula do Aluno:", size=(15, 1)), sg.InputText(key='matricula')],
        [sg.Button("Adicionar"), sg.Button("Cancelar")]
    ]

    novo_aluno_window = sg.Window("Adicionar Aluno", novo_aluno_layout)

    while True:
        add_event, add_values = novo_aluno_window.read()
        if add_event == sg.WINDOW_CLOSED or add_event == "Cancelar":
            novo_aluno_window.close()
            return 0

        if add_event == "Adicionar":
            nome = add_values['nome']
            idade = add_values['idade']
            matricula = add_values['matricula']

            escola.add_aluno(nome, idade, "", matricula, "", [])
            novo_aluno_window.close()
            return 1

    novo_aluno_window.close()
    return 0

def tela_alunos(escola):
    layout = [
        [sg.Text("Lista de Alunos", font=("Arial", 14), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[[aluno.matricula, aluno.nome, aluno.idade] for aluno in escola.Alunos.values()],
                     headings=["Matrícula", "Nome", "Idade"],
                     key="Tabela",
                     auto_size_columns=False,
                     justification='center',
                     font=("Arial", 14),
                     row_height=25)],
        [sg.Button('Adicionar Aluno', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0))),
         sg.Button('Remover Aluno', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0)))],
        [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window("Alunos", layout, finalize=True, size=(450, 400), element_justification='center')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Fechar":
            window.close()
            return 0

        elif event == 'Voltar':
            window.close()
            return 1

        elif event == 'Adicionar Aluno':
            if tela_adicionar_aluno(escola) == 1:
                window['Tabela'].update(values=[[aluno.matricula, aluno.nome, aluno.idade] for aluno in escola.Alunos.values()])

        elif event == 'Remover Aluno':
            selected_row = values['Tabela']
            if selected_row:

                alunos_list = list(escola.Alunos.values())
                aluno_matricula = alunos_list[selected_row[0]].matricula
                del escola.Alunos[aluno_matricula]
                window['Tabela'].update(values=[[aluno.matricula, aluno.nome, aluno.idade] for aluno in escola.Alunos.values()])

    window.close()
    return 0

    window.close()
    return 0
def tela_professores(escola):
    layout = [
        [sg.Text("Lista de Professores", font=("Arial", 14), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[[professor.registro, professor.nome, professor.idade] for professor in escola.Professores.values()],
                     headings=["Registro", "Nome", "Idade"],
                     key="Tabela",
                     auto_size_columns=False,
                     justification='center',
                     font=("Arial", 14),
                     row_height=25)],
        [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window("Professores", layout, finalize=True, size=(450, 400), element_justification='center')

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Fechar":
            window.close()
            return 0
        elif event == 'Voltar':
            window.close()
            return 1

    window.close()
    return 0

def tela_turmas(escola):
    layout = [
        [sg.Text("Lista de Turmas", font=("Arial", 14), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[[turma.nome_turma, len(turma.alunos)] for turma in escola.Turmas.values()],
                     headings=["Turma", "Número de Alunos"],
                     key="Tabela",
                     auto_size_columns=False,
                     justification='center',
                     font=("Arial", 14),
                     row_height=25)],
        [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window("Turmas", layout, finalize=True, size=(450, 400), element_justification='center')

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Fechar":
            window.close()
            return 0
        elif event == 'Voltar':
            window.close()
            return 1

    window.close()
    return 0

