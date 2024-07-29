import PySimpleGUI as sg
from modelo.escola import Materia

# Definindo a configuração de fonte padrão
def fonte_padrao():
    return ("Arial", 14)

def telaInicialSecretario(secretario, escola):
    sg.theme('DarkBlue12')

    layout = [
        [sg.Text('Nome: ' + secretario.nome, font=fonte_padrao()),
         sg.Text('', size=(15, 1)),
         sg.Text(f'Matrícula: ' + str(secretario.registro), font=fonte_padrao())],
        [sg.Text(secretario.email, font=fonte_padrao())],
        [sg.Button("Ver Alunos", key="ALUNOS", size=(15, 1), font=fonte_padrao()),
         sg.Button("Ver Professores", key="PROFESSORES", size=(15, 1), font=fonte_padrao())],
        [sg.Button("Ver Turmas", key="TURMAS", size=(15, 1), font=fonte_padrao()),
         sg.Button("Ver Matérias", key="MATERIAS", size=(15, 1), font=fonte_padrao())]
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
        [sg.Text("Lista de Matérias", font=fonte_padrao(), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[[materia.nome, materia.professor.nome, materia.turma] for materia in materias],
                  headings=["Nome", "Professor", "Turma"],
                  key="Tabela",
                  auto_size_columns=False,
                  justification='center',
                  font=fonte_padrao(),
                  row_height=25)],
        [sg.Button('Voltar', font=fonte_padrao(), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('Fechar', font=fonte_padrao(), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window("Matérias", layout, finalize=True, size=(450, 500), element_justification='center')

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
    turmas = list(escola.Turmas.keys())
    novo_aluno_layout = [
        [sg.Text("Nome do Aluno:", size=(15, 1), font=fonte_padrao()), sg.InputText(key='nome')],
        [sg.Text("Idade do Aluno:", size=(15, 1), font=fonte_padrao()), sg.InputText(key='idade')],
        [sg.Text("Matrícula do Aluno:", size=(15, 1), font=fonte_padrao()), sg.InputText(key='matricula')],
        [sg.Text("Email do Aluno:", size=(15, 1), font=fonte_padrao()), sg.InputText(key='email')],
        [sg.Text("Turma:", size=(15, 1), font=fonte_padrao()), sg.Combo(turmas, key='turma', font=fonte_padrao())],
        [sg.Button("Adicionar", font=fonte_padrao()), sg.Button("Cancelar", font=fonte_padrao())]
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
            email = add_values['email']
            turma_nome = add_values['turma']

            escola.add_aluno(nome, idade, email, matricula, turma_nome, [])
            if turma_nome in escola.Turmas:
                escola.Turmas[turma_nome].alunos.append(matricula)
            novo_aluno_window.close()
            return 1

    novo_aluno_window.close()
    return 0


def tela_alunos(escola):
    layout = [
        [sg.Text("Lista de Alunos", font=fonte_padrao(), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[[aluno.matricula, aluno.nome, aluno.idade] for aluno in escola.Alunos.values()],
                     headings=["Matrícula", "Nome", "Idade"],
                     key="Tabela",
                     auto_size_columns=False,
                     justification='center',
                     font=fonte_padrao(),
                     row_height=25)],
        [sg.Button('Adicionar Aluno', font=fonte_padrao(), size=(15, 1), pad=((5, 5), (10, 0))),
         sg.Button('Remover Aluno', font=fonte_padrao(), size=(15, 1), pad=((5, 5), (10, 0)))],
        [sg.Button('Voltar', font=fonte_padrao(), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('Fechar', font=fonte_padrao(), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window("Alunos", layout, finalize=True, size=(450, 450), element_justification='center')

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

def tela_adicionar_professor(escola):
    layout = [
        [sg.Text("Nome:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='nome')],
        [sg.Text("Idade:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='idade')],
        [sg.Text("Registro:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='matricula')],
        [sg.Text("Email:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='email')],
        [sg.Text("Salário:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='salario')],
        [sg.Button("Adicionar", font=("Arial", 14)), sg.Button("Cancelar", font=("Arial", 14))]
    ]

    window = sg.Window("Adicionar Professor", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            window.close()
            return 0

        if event == "Adicionar":
            nome = values['nome']
            idade = values['idade']
            registro = values['matricula']
            email = values['email']
            salario = values['salario']
            if nome and idade and registro and email and salario:
                escola.add_professor(nome, idade, email, registro,  salario)
                window.close()
                return 1

    window.close()
    return 0



def tela_professores(escola):
    layout = [
        [sg.Text("Lista de Professores", font=fonte_padrao(), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[[professor.registro, professor.nome, professor.idade] for professor in escola.Professores.values()],
                     headings=["Registro", "Nome", "Idade"],
                     key="Tabela",
                     auto_size_columns=False,
                     justification='center',
                     font=fonte_padrao(),
                     row_height=25)],
        [sg.Button('Adicionar Professor', font=fonte_padrao(), size=(15, 1), pad=((5, 5), (10, 0))),
         sg.Button('Remover Professor', font=fonte_padrao(), size=(15, 1), pad=((5, 5), (10, 0)))],
        [sg.Button('Voltar', font=fonte_padrao(), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('Fechar', font=fonte_padrao(), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window("Professores", layout, finalize=True, size=(450, 450), element_justification='center')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Fechar":
            window.close()
            return 0

        elif event == 'Voltar':
            window.close()
            return 1

        elif event == 'Adicionar Professor':
            if tela_adicionar_professor(escola) == 1:
                window['Tabela'].update(values=[[professor.registro, professor.nome, professor.idade] for professor in escola.Professores.values()])

        elif event == 'Remover Professor':
            selected_row = values['Tabela']
            if selected_row:
                professores_list = list(escola.Professores.values())
                professor_registro = professores_list[selected_row[0]].registro
                del escola.Professores[professor_registro]
                window['Tabela'].update(values=[[professor.registro, professor.nome, professor.idade] for professor in escola.Professores.values()])

    window.close()
    return 0


def tela_adicionar_materia(escola):
    professores = [professor.nome for professor in escola.Professores.values()]
    turmas = [turma.nome_turma for turma in escola.Turmas.values()]

    layout = [
        [sg.Text("Nome da Matéria:", size=(15, 1), font=fonte_padrao()), sg.InputText(key='nome')],
        [sg.Text("Professor:", size=(15, 1), font=fonte_padrao()),
         sg.Combo(professores, key='professor', readonly=True, font=fonte_padrao())],
        [sg.Text("Turma:", size=(15, 1), font=fonte_padrao()),
         sg.Combo(turmas, key='turma', readonly=True, font=fonte_padrao())],
        [sg.Button("Adicionar", font=fonte_padrao()), sg.Button("Cancelar", font=fonte_padrao())]
    ]

    window = sg.Window("Adicionar Matéria", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            window.close()
            return 0

        if event == "Adicionar":
            nome = values['nome']
            professor = values['professor']
            turma = values['turma']
            if nome and professor and turma:
                objeto_professor = escola.get_professor_por_nome(professor)
                escola.add_materia(nome, objeto_professor, turma)  # Certifique-se de que a função está correta
                window.close()
                return 1

    window.close()
    return 0


def tela_materias(escola):
    materias = escola.Materias.values()
    layout = [
        [sg.Text("Lista de Matérias", font=fonte_padrao(), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[[materia.nome, materia.professor.nome, materia.turma] for materia in materias],
                  headings=["Nome", "Professor", "Turma"],
                  key="Tabela",
                  auto_size_columns=False,
                  justification='center',
                  font=fonte_padrao(),
                  row_height=25)],
        [sg.Button('Adicionar Matéria', font=fonte_padrao(), size=(15, 1), pad=((5, 5), (10, 0))),
         sg.Button('Voltar', font=fonte_padrao(), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('Fechar', font=fonte_padrao(), size=(10, 1), pad=((5, 5), (10, 0)))]
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

        elif event == 'Adicionar Matéria':
            if tela_adicionar_materia(escola) == 1:
                window['Tabela'].update(values=[[materia.nome, materia.professor.nome, materia.turma] for materia in escola.Materias.values()])

    window.close()
    return 0

def tela_adicionar_turma(escola):
    layout = [
        [sg.Text("Nome da Turma:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='nome')],
        [sg.Button("Adicionar", font=("Arial", 14)), sg.Button("Cancelar", font=("Arial", 14))]
    ]

    window = sg.Window("Adicionar Turma", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            window.close()
            return 0

        if event == "Adicionar":
            nome = values['nome']
            if nome:
                escola.add_turma(nome)
                window.close()
                return 1

    window.close()
    return 0

def tela_turmas(escola):
    turmas = list(escola.Turmas.values())
    layout = [
        [sg.Text("Lista de Turmas", font=fonte_padrao(), pad=((0, 0), (10, 10)))],
        [sg.Table(values=[[turma.nome_turma, len(turma.alunos)] for turma in turmas],
                  headings=["Turma", "Número de Alunos"],
                  key="Tabela",
                  auto_size_columns=False,
                  justification='center',
                  font=fonte_padrao(),
                  row_height=25)],
        [sg.Button('Adicionar Turma', font=fonte_padrao(), size=(15, 1), pad=((5, 5), (10, 0))),
         sg.Button('Remover Turma', font=fonte_padrao(), size=(15, 1), pad=((5, 5), (10, 0)))],
        [sg.Button('Voltar', font=fonte_padrao(), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('Fechar', font=fonte_padrao(), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]

    window = sg.Window("Turmas", layout, finalize=True, size=(450, 450), element_justification='center')

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Fechar":
            window.close()
            return 0

        elif event == 'Voltar':
            window.close()
            return 1

        elif event == 'Adicionar Turma':
            if tela_adicionar_turma(escola) == 1:
                turmas = list(escola.Turmas.values())
                window['Tabela'].update(values=[[turma.nome_turma, len(turma.alunos)] for turma in turmas])

        elif event == 'Remover Turma':
            selected_row = values['Tabela']
            if selected_row:
                turma_nome = turmas[selected_row[0]].nome_turma
                escola.remove_turma(turma_nome)
                turmas = list(escola.Turmas.values())
                window['Tabela'].update(values=[[turma.nome_turma, len(turma.alunos)] for turma in turmas])

    window.close()
    return 0