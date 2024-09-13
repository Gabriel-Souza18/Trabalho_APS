import PySimpleGUI as sg

class TelaProfessor:
    def __init__(self, controlador):
        self.controlador = controlador

    def tela_professor(self, professor):
        sg.theme('DarkBlue12')
        layout = [
            [sg.Text(f'Nome: {professor.nome}', font=("Arial", 14)),
             sg.Text('', size=(15, 1)),
             sg.Text(f'Registro: {professor.registro}', font=("Arial", 14))],
            [sg.Text(f'Email: {professor.email}', font=("Arial", 14))],
            [sg.Button("Ver Matérias", key="MATERIAS", size=(15, 1), font=("Arial", 14)),
             sg.Button("Ver Turmas", key="TURMAS", size=(15, 1), font=("Arial", 14))]
        ]
        window =  sg.Window("Tela Inicial do Professor", layout, size=(450, 150), element_justification='center', finalize=True)


        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == 'MATERIAS':
                lista_materias = self.controlador.obter_materias(professor)
                self.tela_materias(professor, lista_materias)

            elif event == 'TURMAS':
                turmas = self.controlador.obter_turmas_professor(professor)
                self.tela_turmas(professor, turmas)

        window.close()

    def tela_materias(self, professor, lista_materias):
        linhas_tabela = []
        for materia in lista_materias:
            if not hasattr(materia, 'provas') or not hasattr(materia, 'trabalhos'):
                continue

            linhas_tabela.append([materia.nome])

        layout = [
            [sg.Text("Clique na matéria para ver detalhes", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Table(values=linhas_tabela,
                      headings=["Matéria"],
                      key="Tabela",
                      auto_size_columns=False,
                      col_widths=[20],
                      justification='center',
                      enable_events=True,
                      font=("Arial", 14),
                      row_height=25)],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
             sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]
        
        window = sg.Window('Matérias', layout, finalize=True, size=(400, 400), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            if event == 'Tabela':
                linha_clicada = values['Tabela'][0] if values['Tabela'] else None
                if linha_clicada is not None:
                    materia = lista_materias[linha_clicada]
                    self.tela_materia(materia, professor)

        window.close()

    def tela_turmas(self, professor, turmas):
        linhas_tabela = [[turma.nome_turma] for turma in turmas]
        linhas_tabela.sort(key=lambda x: x[0])

        layout = [
            [sg.Text(f"Turmas do Professor: {professor.nome}", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Table(values=linhas_tabela,
                      headings=["Turma"],
                      key="Tabela",
                      auto_size_columns=False,
                      col_widths=[20],
                      justification='center',
                      display_row_numbers=True,
                      enable_events=True,
                      font=("Arial", 14),
                      row_height=25)],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
             sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]
        
        window = sg.Window("Turmas", layout, finalize=True, size=(400, 400), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            if event == 'Tabela':
                linha_clicada = values['Tabela'][0] if values['Tabela'] else None
                if linha_clicada is not None:
                    turma = turmas[linha_clicada]
                    self.tela_alunos(turma)

            elif event == 'Voltar':
                window.close()
                return

        window.close()

    def tela_materia(self, materia, professor):
        dados_arvore = sg.TreeData()

        dados_arvore.insert("", "CP", "Provas", [('')])
        for prova, valor in materia.provas.items():
            dados_arvore.insert("CP", prova, prova, [f"{valor}"])

        dados_arvore.insert("", "CT", "Trabalhos", [('')])
        for trabalho, valor in materia.trabalhos.items():
            dados_arvore.insert("CT", trabalho, trabalho, [f"{valor}"])

        layout = [
            [sg.Text(f"{materia.nome} - Professor: {professor.nome}", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Tree(data=dados_arvore,
                     headings=["Valor"],
                     key="Arvore",
                     auto_size_columns=False,
                     col_widths=[30],
                     justification='center',
                     font=("Arial", 14),
                     row_height=25)],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
             sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))],
             [sg.Button('Adicionar Nota', key='ADICIONAR_NOTA', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0))),
             sg.Button('Ver Alunos', key='VER_ALUNOS', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0)))]
        ]

        window = sg.Window("Matéria", layout, finalize=True, size=(500, 450), element_justification='center')


        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            elif event == 'ADICIONAR_NOTA':
                self.tela_adicionar_nota(materia)

            elif event == 'VER_ALUNOS':
                self.tela_alunos(materia)

        window.close()

    def tela_adicionar_nota(self, materia):
        layout = [
            [sg.Text('Adicionar Nota ou Prova', font=("Arial", 14))],
            [sg.Text('Tipo:', font=("Arial", 12)), sg.Combo(['Prova', 'Trabalho'], key='Tipo', size=(20, 1))],
            [sg.Text('Nome:', font=("Arial", 12)), sg.InputText(key='Nome', size=(20, 1))],
            [sg.Text('Nota:', font=("Arial", 12)), sg.InputText(key='Nota', size=(20, 1))],
            [sg.Button('Adicionar', font=("Arial", 14), size=(10, 1)),
            sg.Button('Cancelar', font=("Arial", 14), size=(10, 1))]
        ]

        window = sg.Window('Adicionar Nota ou Prova', layout, finalize=True, size=(300, 200), element_justification='center')

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                break

            if event == 'Adicionar':
                tipo = values['Tipo']
                nome = values['Nome']
                nota = values['Nota']

                if tipo and nome and nota:
                    self.controlador.atribuir_atividade_para_todos_alunos(materia.nome, tipo, nome, float(nota))
                    sg.popup('Atividade adicionada com sucesso!')
                else:
                    sg.popup_error('Todos os campos são obrigatórios.')

        window.close()


    def tela_alunos(self, turma):
        lista_alunos = self.controlador.obter_alunos_por_turma(turma)
        linhas_tabela = [[aluno.matricula, aluno.nome] for aluno in lista_alunos]
        linhas_tabela.sort(key=lambda x: x[1])

        layout = [
            [sg.Text(f"Alunos da Turma: {turma.nome_turma}", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Table(values=linhas_tabela,
                    headings=["Matrícula", "Nome"],
                    key="Tabela",
                    auto_size_columns=False,
                    col_widths=[15, 25],
                    justification='center',
                    display_row_numbers=True,
                    font=("Arial", 14),
                    row_height=25,
                    enable_events=True)],  # Certifique-se de que os eventos estão ativados
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
            sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]

        window = sg.Window("Alunos", layout, finalize=True, size=(500, 400), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            if event == 'Tabela':
                if values['Tabela']:  # Verifica se há uma linha selecionada
                    linha_clicada = values['Tabela'][0]  # Obtém a linha clicada
                    aluno = lista_alunos[linha_clicada]
                    # Abre a tela para atribuir notas faltantes
                    self.tela_selecionar_materia_para_atribuir_notas(aluno)

            elif event == 'Voltar':
                window.close()
                return

        window.close()

    def tela_selecionar_materia_para_atribuir_notas(self, aluno):
        # Obtém as matérias do aluno
        materias = self.controlador.obter_materias_do_aluno(aluno)
        lista_materias = [materia.nome for materia in materias]

        layout = [
            [sg.Text(f"Selecionar matéria para o aluno: {aluno.nome}", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Combo(lista_materias, key="Materia", font=("Arial", 14), size=(30, 1))],
            [sg.Button('Verificar e Atribuir Notas', font=("Arial", 14), size=(20, 1), pad=((5, 5), (10, 0))),
            sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]

        window = sg.Window("Selecionar Matéria", layout, finalize=True, size=(500, 300), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Voltar'):
                break

            if event == 'Verificar e Atribuir Notas':
                materia_nome = values['Materia']
                if materia_nome:
                    self.tela_atribuir_notas_faltantes(aluno, materia_nome)
                else:
                    sg.popup("Por favor, selecione uma matéria.", title="Erro")

        window.close()

    def tela_atribuir_notas_faltantes(self, aluno, materia_nome):
        # Obtém a matéria e suas atividades
        materia = self.controlador.materia_dao.buscar_materia(materia_nome)
        if not materia:
            sg.popup(f"Matéria {materia_nome} não encontrada.", title="Erro")
            return

        # Verifica atividades pendentes
        atividades_pendentes = {}
        for tipo_atividade, atividades in materia.provas.items():
            if isinstance(atividades, dict):  # Verifica se é um dicionário
                for atividade, valor in atividades.items():
                    if atividade not in aluno.notas.get(materia_nome, {}).get(tipo_atividade, {}):
                        atividades_pendentes[atividade] = tipo_atividade

        if atividades_pendentes:
            # Solicita nota para as atividades pendentes
            for atividade, tipo in atividades_pendentes.items():
                nota = sg.popup_get_text(f"Digite a nota para a atividade '{atividade}' ({tipo}) do aluno {aluno.nome}:")
                if nota:
                    try:
                        nota = float(nota)
                        self.controlador.atribuir_nota_aluno(aluno, materia_nome, atividade, nota)
                    except ValueError:
                        sg.popup("Nota deve ser um número válido.", title="Erro")
        else:
            sg.popup("O aluno já possui todas as notas lançadas.", title="Informação")
