import PySimpleGUI as sg

class TelaSecretario:
    def __init__(self, controlador):
        self.controlador = controlador

    def tela_inicial(self, secretario):
        sg.theme('DarkBlue12')
        layout = [
            [sg.Text(f'Nome: {secretario.nome}', font=("Arial", 14)),
             sg.Text('', size=(15, 1)),
             sg.Text(f'Matrícula: {secretario.registro}', font=("Arial", 14))],
            [sg.Text(secretario.email, font=("Arial", 14))],
            [sg.Button("Ver Alunos", key="ALUNOS", size=(15, 1), font=("Arial", 14)),
             sg.Button("Ver Professores", key="PROFESSORES", size=(15, 1), font=("Arial", 14))],
            [sg.Button("Ver Turmas", key="TURMAS", size=(15, 1), font=("Arial", 14)),
             sg.Button("Ver Matérias", key="MATERIAS", size=(15, 1), font=("Arial", 14))],
            [sg.Button("Ver Secretários", key="SECRETARIOS", size=(15, 1), font=("Arial", 14))]
        ]
        
        window = sg.Window("Secretário", layout, size=(450, 250), element_justification='center', finalize=True)


        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == "ALUNOS":
                self.tela_alunos()

            elif event == "PROFESSORES":
                self.tela_professores()

            elif event == "TURMAS":
                self.tela_turmas()

            elif event == "MATERIAS":
                self.tela_materias()

            elif event == "SECRETARIOS":
                self.tela_secretarios()

        window.close()

    #----------------------------------------------------------------------
    # PARTE DO SECRETARIO
    #----------------------------------------------------------------------

    def tela_secretarios(self):
        secretarios = self.controlador.obter_secretarios()
        linhas_tabela = [[secretario.registro, secretario.nome, secretario.idade] for secretario in secretarios]

        layout = [
            [sg.Text("Lista de Secretários", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Table(values=linhas_tabela,
                      headings=["Registro", "Nome", "Idade"],
                      key="Tabela",
                      auto_size_columns=False,
                      justification='center',
                      font=("Arial", 14),
                      row_height=25,
                      enable_events=True,
                      select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button('Adicionar Secretário', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0))),
             sg.Button('Remover Secretário', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0)))],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
             sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]

        window = sg.Window("Secretários", layout, finalize=True, size=(450, 450), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            elif event == 'Adicionar Secretário':
                self.tela_adicionar_secretario()
                window['Tabela'].update(values=[[sec.registro, sec.nome, sec.idade] for sec in self.controlador.obter_secretarios()])


            elif event == 'Remover Secretário':
                selected_row = values['Tabela']
                if selected_row:
                    selected_row_index = selected_row[0] if isinstance(selected_row, list) else selected_row 
                    secretarios = list(self.controlador.obter_secretarios()) 
                    if 0 <= selected_row_index < len(secretarios): 
                        secretario = secretarios[selected_row_index]
                        secretario_registro = secretario.registro
                        self.controlador.remover_secretario(secretario_registro)
                        window['Tabela'].update(values=[[sec.registro, sec.nome, sec.idade] for sec in self.controlador.obter_secretarios()])

        window.close()

    def tela_adicionar_secretario(self):
        layout = [
            [sg.Text("Nome:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='nome')],
            [sg.Text("Idade:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='idade')],
            [sg.Text("Registro:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='registro')],
            [sg.Text("Salario:", size=(15,1), font=("Arial", 14)), sg.InputText(key='salario')],
            [sg.Text("Email:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='email')],
            [sg.Button("Adicionar", font=("Arial", 14)), sg.Button("Cancelar", font=("Arial", 14))]
        ]

        window = sg.Window("Adicionar Secretário", layout, finalize=True)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return False

            if event == 'Adicionar':
                nome = values['nome']
                idade = values['idade']
                registro = values['registro']
                salario = values['salario']
                email = values['email']
                if nome and idade and registro and email and salario:
                    self.controlador.adicionar_secretario(nome, idade, salario, email, registro)
                    window.close()
                    return True

        window.close()
    
    #----------------------------------------------------------------------
    # PARTE DO ALUNO
    #----------------------------------------------------------------------

    def tela_alunos(self):
        alunos = self.controlador.obter_alunos()
        
        alunos_lista = [[aluno.matricula, aluno.nome, aluno.idade] for aluno in alunos]
        
        layout = [
            [sg.Text("Lista de Alunos", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Table(values=alunos_lista,
                    headings=["Matricula", "Nome", "Idade"],
                    key="Tabela",
                    auto_size_columns=False,
                    justification='center',
                    font=("Arial", 14),
                    row_height=25,
                    enable_events=True,
                    select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button('Adicionar Aluno', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0))),
            sg.Button('Remover Aluno', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0)))],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
            sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]
    
        window = sg.Window("Alunos", layout, finalize=True, size=(450, 450), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            elif event == 'Adicionar Aluno':
                turmas = self.controlador.obter_turmas()
                self.tela_adicionar_aluno(turmas)
                window['Tabela'].update(values=[[aluno.matricula, aluno.nome, aluno.idade] for aluno in self.controlador.obter_alunos()])


            elif event == 'Remover Aluno':
                selected_row = values['Tabela']
                if selected_row:
                    selected_row_index = selected_row[0] if isinstance(selected_row, list) else selected_row  # Garante que é um índice
                    alunos = list(self.controlador.obter_alunos()) 
                    if 0 <= selected_row_index < len(alunos): 
                        aluno = alunos[selected_row_index]
                        aluno_matricula = aluno.matricula
                        self.controlador.remover_aluno(aluno_matricula)
                        window['Tabela'].update(values=[[aluno.matricula, aluno.nome, aluno.idade] for aluno in self.controlador.obter_alunos()])

        window.close()

    def tela_adicionar_aluno(self, turmas):
        turmas_nomes = [turma.nome_turma for turma in turmas]

        layout = [
            [sg.Text("Nome:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='nome')],
            [sg.Text("Idade:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='idade')],
            [sg.Text("Matricula:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='matricula')],
            [sg.Text("Email:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='email')],
            [sg.Text("Turma:", size=(15, 1), font=("Arial", 14)), sg.Combo(turmas_nomes, key='turma')],
            [sg.Button("Adicionar", font=("Arial", 14)), sg.Button("Cancelar", font=("Arial", 14))]
        ]
        
        window = sg.Window("Adicionar Aluno", layout, finalize=True)

        turmas = self.controlador.obter_turmas()

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return False

            if event == 'Adicionar':
                nome = values['nome']
                idade = values['idade']
                matricula = values['matricula']
                email = values['email']
                turma = values['turma']
                if nome and idade and matricula and email and turma:
                    self.controlador.adicionar_aluno(nome, idade, email, matricula, turma)
                    window.close()
                    return True

        window.close()
    
    #----------------------------------------------------------------------
    # PARTE DO PROFESSOR
    #----------------------------------------------------------------------

    def tela_professores(self):
        professores = self.controlador.obter_professores()
        
        professores_lista = [[professor.registro, professor.nome, professor.idade] for professor in professores]
        
        layout = [
            [sg.Text("Lista de Professores", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Table(values=professores_lista,
                    headings=["Registro", "Nome", "Idade"],
                    key="Tabela",
                    auto_size_columns=False,
                    justification='center',
                    font=("Arial", 14),
                    row_height=25,
                    enable_events=True,
                    select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button('Adicionar Professor', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0))),
            sg.Button('Remover Professor', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0)))],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
            sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]

        window = sg.Window("Professores", layout, finalize=True, size=(450, 450), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            elif event == 'Adicionar Professor':
                self.tela_adicionar_professor()
                window['Tabela'].update(values=[[prof.registro, prof.nome, prof.idade] for prof in self.controlador.obter_professores()])


            elif event == 'Remover Professor':
                selected_row = values['Tabela']
                if selected_row:
                    selected_row_index = selected_row[0] if isinstance(selected_row, list) else selected_row  # Garante que é um índice
                    professores = list(self.controlador.obter_professores()) 

                    if 0 <= selected_row_index < len(professores): 
                        professor = professores[selected_row_index]
                        professor_registro = professor.registro
                        self.controlador.remover_professor(professor_registro)
                        window['Tabela'].update(values=[[prof.registro, prof.nome, prof.idade] for prof in self.controlador.obter_professores()])

        window.close()

    def tela_adicionar_professor(self):
        layout = [
            [sg.Text("Nome:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='nome')],
            [sg.Text("Idade:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='idade')],
            [sg.Text("Registro:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='registro')],
            [sg.Text("Salario:", size=(15,1), font=("Arial", 14)), sg.InputText(key='salario')],
            [sg.Text("Email:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='email')],
            [sg.Button("Adicionar", font=("Arial", 14)), sg.Button("Cancelar", font=("Arial", 14))]
        ]

        window = sg.Window("Adicionar Professor", layout, finalize=True)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return False

            if event == 'Adicionar':
                nome = values['nome']
                idade = values['idade']
                registro = values['registro']
                salario = values['salario']
                email = values['email']
                if nome and idade and registro and email and salario:
                    self.controlador.adicionar_professor(nome, idade, email, salario, registro)
                    window.close()
                    return True

        window.close()

    #----------------------------------------------------------------------
    # PARTE DAS MATERIAS
    #----------------------------------------------------------------------


    def tela_materias(self):
        materias = self.controlador.obter_materias() 
        materias_lista = [[materia.nome, materia.professor.nome, materia.turma.nome_turma] for materia in materias]

        layout = [
            [sg.Text("Lista de Matérias", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Table(values=materias_lista,
                      headings=["Nome", "Professor", "Turma"],
                      key="TabelaMaterias",
                      auto_size_columns=False,
                      justification='center',
                      font=("Arial", 14),
                      row_height=25,
                      enable_events=True,
                      select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button('Adicionar Matéria', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0))),
             sg.Button('Remover Matéria', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0)))],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
             sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]

        window = sg.Window("Matérias", layout, finalize=True, size=(600, 450), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, 'Fechar'):
                break

            elif event == 'Adicionar Matéria':
                self.tela_adicionar_materia()
                window['TabelaMaterias'].update(
                    values=[[materia.nome, materia.professor, materia.turma] for materia in self.controlador.obter_materias()])

            elif event == 'Remover Matéria':
                selected_row = values['TabelaMaterias']
                if selected_row:
                    selected_row_index = selected_row[0] if isinstance(selected_row, list) else selected_row
                    materias = list(self.controlador.obter_materias())

                    if 0 <= selected_row_index < len(materias):
                        materia = materias[selected_row_index]
                        self.controlador.remover_materia(materia.nome)
                        window['TabelaMaterias'].update(
                            values=[[materia.nome, materia.professor.nome, materia.turma.nome_turma] for materia in self.controlador.obter_materias()])

        window.close()

    def tela_adicionar_materia(self):
        professores = [professor.nome for professor in self.controlador.obter_professores()]
        turmas = [turma.nome_turma for turma in self.controlador.obter_turmas()]

        layout = [
            [sg.Text("Nome da Matéria:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='nome')],
            [sg.Text("Nome do Professor:", size=(15, 1), font=("Arial", 14)), sg.Combo(professores, key='professor', readonly=True)],
            [sg.Text("Nome da Turma:", size=(15, 1), font=("Arial", 14)), sg.Combo(turmas, key='turma', readonly=True)],
            [sg.Button("Adicionar", font=("Arial", 14)), sg.Button("Cancelar", font=("Arial", 14))]
        ]

        window = sg.Window("Adicionar Matéria", layout, finalize=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                window.close()
                return False

            if event == 'Adicionar':
                nome = values['nome']
                professor = values['professor']
                turma = values['turma']
                if nome and professor and turma:
                    self.controlador.adicionar_materia(turma, nome, professor)
                    window.close()
                    return True

        window.close() 

    #----------------------------------------------------------------------
    # PARTE DAS TURMAS
    #----------------------------------------------------------------------


    def tela_turmas(self):
        turmas = self.controlador.obter_turmas()
        turmas_lista = [[turma.nome_turma, len(turma.alunos), len(turma.materias)] for turma in turmas]

        layout = [
            [sg.Text("Lista de Turmas", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Table(values=turmas_lista,
                      headings=["Nome", "Nº de Alunos", "Nº de Matérias"],
                      key="TabelaTurmas",
                      auto_size_columns=False,
                      justification='center',
                      font=("Arial", 14),
                      row_height=25,
                      enable_events=True,
                      select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Button('Adicionar Turma', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0))),
             sg.Button('Remover Turma', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0)))],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
             sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]

        window = sg.Window("Turmas", layout, finalize=True, size=(600, 450), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, 'Fechar'):
                break

            elif event == 'Adicionar Turma':
                self.tela_adicionar_turma()
                window['TabelaTurmas'].update(
                    values=[[turma.nome_turma, len(turma.alunos), len(turma.materias)] for turma in self.controlador.obter_turmas()])

            elif event == 'Remover Turma':
                selected_row = values['TabelaTurmas']
                if selected_row:
                    selected_row_index = selected_row[0]
                    turmas = list(self.controlador.obter_turmas())

                    if 0 <= selected_row_index < len(turmas):
                        turma = turmas[selected_row_index]
                        self.controlador.remover_turma(turma.nome_turma)
                        window['TabelaTurmas'].update(
                            values=[[turma.nome_turma, len(turma.alunos), len(turma.materias)] for turma in self.controlador.obter_turmas()])

        window.close()

    def tela_adicionar_turma(self):
        layout = [
            [sg.Text("Nome da Turma:", size=(15, 1), font=("Arial", 14)), sg.InputText(key='nome_turma')],
            [sg.Button("Adicionar", font=("Arial", 14)), sg.Button("Cancelar", font=("Arial", 14))]
        ]

        window = sg.Window("Adicionar Turma", layout, finalize=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                window.close()
                return False

            if event == 'Adicionar':
                nome_turma = values['nome_turma']
                if nome_turma:
                    self.controlador.adicionar_turma(nome_turma)
                    window.close()
                    return True

        window.close()
