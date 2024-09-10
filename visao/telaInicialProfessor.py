import PySimpleGUI as sg

def fonte_padrao():
    return ("Arial", 14)

def TelaInicialProfessor(professor, escola):
    """
    Exibe a tela inicial do professor com opções para ver turmas e matérias.
    
    :param professor: Instância da classe Professor
    :param escola: Instância da classe Escola
    """
    sg.theme('DarkBlue12')

    layout = [
        [sg.Text('Nome: ' + professor.nome, font=fonte_padrao()),
         sg.Text('', size=(15, 1)),
         sg.Text(f'Registro: ' + str(professor.registro), font=fonte_padrao())],
        [sg.Text(professor.email, font=fonte_padrao())],
        [sg.Button("Ver Turmas", key="TURMAS", size=(15, 1), font=fonte_padrao()), 
         sg.Button("Ver Matérias", key="MATERIAS", size=(15, 1), font=fonte_padrao())]
    ]
    
    window = sg.Window("Professor", layout, size=(500, 150), element_justification='center', finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == "TURMAS":
            window.close()
            tela_turmas(professor, escola)

        if event == "MATERIAS":
            window.close()
            tela_materias(professor, escola)
    
    window.close()

def tela_turmas(professor, escola):
    """
    Exibe a tela com a lista de turmas que o professor leciona.
    
    :param professor: Instância da classe Professor
    :param escola: Instância da classe Escola
    """
    turmas = escola.get_turmas_do_professor(professor)
    turmas_info = [[turma.nome_turma, len(turma.alunos)] for turma in turmas]

    layout = [
        [sg.Text("Turmas do Professor", font=("Arial", 16, "bold"), justification='center', expand_x=True)],
        [sg.Text("", size=(40, 1))],  # Espaço para melhorar a estética
        [sg.Table(values=turmas_info,
                  headings=["Nome da Turma", "Quantidade de Alunos"],
                  auto_size_columns=True,
                  justification='center',
                  key="TabelaTurmas",
                  font=("Arial", 14),
                  row_height=30,
                  enable_events=True,
                  num_rows=min(len(turmas_info), 10))],  # Limita o número de linhas visíveis
        [sg.Text("", size=(40, 1))],  # Espaço para melhorar a estética
        [sg.Button('Voltar', font=("Arial", 14), pad=((10, 5), (10, 5))),
         sg.Button('Fechar', font=("Arial", 14), pad=((5, 10), (10, 5)))],
        [sg.Text("", size=(40, 1))]  # Espaço para melhorar a estética
    ]

    window = sg.Window("Turmas", layout, size=(500, 200), finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Fechar'):
            break
        elif event == 'Voltar':
            window.close()
            TelaInicialProfessor(professor, escola)
            return
        elif event == 'TabelaTurmas':
            if values['TabelaTurmas']:
                selected_row = values['TabelaTurmas'][0]
                turma_selecionada = turmas[selected_row]
                tela_alunos_da_turma(escola, turma_selecionada, professor)

    window.close()

def tela_alunos_da_turma(escola, turma, professor):
    """
    Exibe a tela com a lista de alunos da turma selecionada e permite a atribuição de notas.
    
    :param escola: Instância da classe Escola
    :param turma: Instância da classe Turma
    :param professor: Instância da classe Professor
    """
    alunos_info = [[aluno.matricula, aluno.nome, aluno.idade] for aluno in turma.alunos]
    
    layout = [
        [sg.Text(f"Alunos da {turma.nome_turma}", font=("Arial", 16, "bold"), justification='center', expand_x=True, pad=((0, 0), (10, 10)))],
        [sg.Text("", size=(40, 1))],  # Espaço para melhorar a estética
        [sg.Table(values=alunos_info,
                  headings=["Matrícula", "Nome", "Idade"],
                  auto_size_columns=True,
                  justification='center',
                  key="TabelaAlunos",
                  font=("Arial", 14),
                  row_height=30,
                  enable_events=True,
                  select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                  num_rows=min(len(alunos_info), 10))],  # Limita o número de linhas visíveis
        [sg.Text("", size=(40, 1))],  # Espaço para melhorar a estética
        [sg.Button('Voltar', font=("Arial", 14), pad=((10, 5), (10, 5))),
         sg.Button('Fechar', font=("Arial", 14), pad=((5, 10), (10, 5)))],
        [sg.Text("", size=(40, 1))]  # Espaço para melhorar a estética
    ]

    window = sg.Window("Alunos da Turma", layout, size=(500, 250), finalize=True, element_justification='center')

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Fechar':
            break
        elif event == 'Voltar':
            window.close()
            tela_turmas(professor, escola) 
            return
        elif event == 'TabelaAlunos':
            window['AdicionarNota'].update(disabled=False)

    window.close()


def tela_materias(professor, escola):
    """
    Exibe a tela com a lista de matérias que o professor leciona.
    
    :param professor: Instância da classe Professor
    :param escola: Instância da classe Escola
    """
    materias = escola.get_materias_do_professor(professor)
    materias_info = [[materia.nome, materia.turma.nome_turma] for materia in materias]

    layout = [
        [sg.Text("Matérias do Professor", font=("Arial", 16, "bold"), justification='center', expand_x=True)],
        [sg.Text("", size=(40, 1))],
        [sg.Table(values=materias_info,
                  headings=["Matéria", "Turma"],
                  auto_size_columns=True,
                  justification='center',
                  key="TabelaMaterias",
                  font=("Arial", 14),
                  row_height=30,
                  enable_events=True,
                  num_rows=min(len(materias_info), 10),
                  expand_x=True)],
        [sg.Text("", size=(40, 1))], 
        [sg.Button('Voltar', font=("Arial", 14), pad=((0, 10), (0, 10))),
         sg.Button('Fechar', font=("Arial", 14), pad=((10, 0), (0, 10)))],
        [sg.Text("", size=(40, 1))]
    ]


    window = sg.Window("Matérias", layout, size=(500, 200), finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Fechar'):
            break
        elif event == 'Voltar':
            window.close()
            TelaInicialProfessor(professor, escola)
            return
        elif event == 'TabelaMaterias':
            if values['TabelaMaterias']:
                selected_row = values['TabelaMaterias'][0]
                materia_selecionada = materias[selected_row]
                tela_opcoes_materia(materia_selecionada, escola, professor)

    window.close()

def tela_opcoes_materia(materia, escola, professor):
    """
    Exibe opções para adicionar provas e trabalhos à matéria selecionada.
    
    :param materia: Instância da classe Materia
    :param escola: Instância da classe Escola
    :param professor: Instância da classe Professor
    """
    sg.theme('DarkBlue12')

    layout = [
        [sg.Text(f"Opções para a Matéria: {materia.nome}", font=("Arial", 16, "bold"), justification='center', expand_x=True)],
        [sg.Text("", size=(40, 1))], 
        [sg.Button('Adicionar Prova', font=("Arial", 14), pad=((10, 5), (10, 5))),
         sg.Button('Adicionar Trabalho', font=("Arial", 14), pad=((5, 10), (10, 5)))],
        [sg.Text("", size=(40, 1))],  
        [sg.Button('Voltar', font=("Arial", 14), pad=((10, 5), (10, 5))),
         sg.Button('Fechar', font=("Arial", 14), pad=((5, 10), (10, 5)))],
        [sg.Text("", size=(40, 1))] 
    ]

    window = sg.Window(f"Opções da Matéria: {materia.nome}", layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Fechar'):
            break
        elif event == 'Voltar':
            window.close()
            tela_materias(professor, escola)
            return
        elif event == 'Adicionar Prova':
            tela_atribuir_atividade(escola, materia, "Prova", professor)
        elif event == 'Adicionar Trabalho':
            tela_atribuir_atividade(escola, materia, "Trabalho", professor)

    window.close()


def tela_atribuir_atividade(escola, materia, tipo_atividade, professor):
    """
    Tela para atribuir uma atividade (prova/trabalho) e adicionar notas para os alunos da turma.
    
    :param escola: Instância da classe Escola
    :param materia: Instância da classe Materia
    :param tipo_atividade: Tipo da atividade (Prova ou Trabalho)
    :param professor: Instância da classe Professor
    """
    sg.theme('DarkBlue12')
    
    layout = [
        [sg.Text(f"Atribuir {tipo_atividade} - {materia.nome}", font=("Arial", 16, "bold"), justification='center', expand_x=True)],
        [sg.Text("", size=(40, 1))],  
        [sg.Text("Nome da Atividade:", font=("Arial", 14), pad=((10, 5), (10, 5))),
         sg.InputText(key='nome_atividade', font=("Arial", 14), size=(30, 1), pad=((5, 10), (10, 5)))],
        [sg.Text("Nota Máxima:", font=("Arial", 14), pad=((10, 5), (10, 5))),
         sg.InputText(key='nota_maxima', font=("Arial", 14), size=(10, 1), pad=((5, 10), (10, 5)))],
        [sg.Text("", size=(40, 1))], 
        [sg.Button("Confirmar", key="CONFIRMAR", font=("Arial", 14), pad=((10, 5), (10, 5))),
         sg.Button("Cancelar", key="CANCELAR", font=("Arial", 14), pad=((5, 10), (10, 5)))],
        [sg.Text("", size=(40, 1))]  
    ]
    
    window = sg.Window("Atribuir Atividade", layout, size=(400, 250), element_justification='center', finalize=True)
    
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "CANCELAR":
            window.close()
            break
        
        if event == "CONFIRMAR":
            nome_atividade = values['nome_atividade']
            try:
                nota_maxima = float(values['nota_maxima'])
            except ValueError:
                sg.popup("Nota máxima inválida. Por favor, insira um número válido.")
                continue
            
            # Atualiza a matéria
            if tipo_atividade == "Prova":
                materia.provas[nome_atividade] = nota_maxima
            elif tipo_atividade == "Trabalho":
                materia.trabalhos[nome_atividade] = nota_maxima
            
            # Atualiza a lista de alunos da turma
            turma = escola.get_turma_por_nome(materia.turma.nome_turma)
            if turma:
                alunos = turma.alunos
                
                for aluno in alunos:
                    if materia.nome not in aluno.notas:
                        aluno.notas[materia.nome] = {"provas": {}, "trabalhos": {}}
                    if tipo_atividade == "Prova":
                        aluno.notas[materia.nome]["provas"][nome_atividade] = 0
                    elif tipo_atividade == "Trabalho":
                        aluno.notas[materia.nome]["trabalhos"][nome_atividade] = 0
            
                # Tela para adicionar notas aos alunos
                tela_adicionar_notas(escola, turma, materia, tipo_atividade, nome_atividade)

            window.close()
            break

def tela_adicionar_notas(escola, turma, materia, tipo_atividade, nome_atividade):
    """
    Tela para adicionar notas para os alunos da turma após a atribuição da atividade.
    
    :param escola: Instância da classe Escola
    :param turma: Instância da classe Turma
    :param materia: Instância da classe Materia
    :param tipo_atividade: Tipo da atividade (Prova ou Trabalho)
    :param nome_atividade: Nome da atividade
    """
    alunos = turma.alunos
    aluno_info = {aluno.matricula: aluno.nome for aluno in alunos}

    layout = [
        [sg.Text(f"Adicionar Notas para a Turma {turma.nome_turma}", font=("Arial", 16, "bold"), justification='center', expand_x=True)],
        [sg.Text("", size=(40, 1))], 
        [sg.Text("Matrícula", font=("Arial", 14), size=(10, 1)),
         sg.Text("Nome", font=("Arial", 14), size=(20, 1)),
         sg.Text("Nota", font=("Arial", 14), size=(10, 1))],
        [sg.Text("", size=(40, 1))], 
        [sg.Text("", size=(40, 1))],  
        [sg.Button("Confirmar", key="CONFIRMAR", font=("Arial", 14), pad=((10, 5), (10, 5))),
         sg.Button("Cancelar", key="CANCELAR", font=("Arial", 14), pad=((5, 10), (10, 5)))],
        [sg.Text("", size=(40, 1))] 
    ]
    for matricula, nome in aluno_info.items():
        layout.append([
            sg.Text(matricula, font=("Arial", 14)),
            sg.Text(nome, font=("Arial", 14)),
            sg.InputText(key=f'{matricula}_nota', font=("Arial", 14))
        ])

    layout.append([
        sg.Button("Salvar Notas", key="SALVAR", font=("Arial", 14)),
        sg.Button("Cancelar", key="CANCELAR", font=("Arial", 14))
    ])

    window = sg.Window("Adicionar Notas", layout, size=(600, 400), element_justification='center', finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "CANCELAR":
            window.close()
            break
        
        if event == "SALVAR":
            notas_invalidas = []
            for matricula, nome in aluno_info.items():
                chave_nota = f'{matricula}_nota'
                if chave_nota in values:
                    try:
                        nota = float(values[chave_nota])
                        aluno = escola.get_aluno(matricula)
                        if aluno:
                            if tipo_atividade == "Prova":
                                aluno.notas[materia.nome]["provas"][nome_atividade] = nota
                            elif tipo_atividade == "Trabalho":
                                aluno.notas[materia.nome]["trabalhos"][nome_atividade] = nota
                    except ValueError:
                        notas_invalidas.append(nome)
            
            if notas_invalidas:
                sg.popup(f"Nota inválida para os alunos: {', '.join(notas_invalidas)}.")
            else:
                sg.popup("Notas salvas com sucesso!")
            
            window.close()
            break