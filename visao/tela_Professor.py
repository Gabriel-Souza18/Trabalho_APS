import PySimpleGUI as sg

class TelaProfessor:
    def __init__(self, controlador):
        self.controlador = controlador

    def layout_tela_professor(self, professor):
        sg.theme('DarkBlue12')
        layout = [
            [sg.Text(f'Nome: {professor.nome}', font=("Arial", 14)),
             sg.Text('', size=(15, 1)),
             sg.Text(f'Registro: {professor.registro}', font=("Arial", 14))],
            [sg.Text(f'Email: {professor.email}', font=("Arial", 14))],
            [sg.Button("Ver Matérias", key="MATERIAS", size=(15, 1), font=("Arial", 14)),
             sg.Button("Ver Turmas", key="TURMAS", size=(15, 1), font=("Arial", 14))]
        ]
        return sg.Window("Tela Inicial do Professor", layout, size=(450, 150), element_justification='center', finalize=True)

    def iniciar_tela_professor(self, professor):
        window = self.layout_tela_professor(professor)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == 'MATERIAS':
                self.iniciar_tela_materias(professor)

            elif event == 'TURMAS':
                self.iniciar_tela_turmas(professor)

        window.close()

    def layout_tela_materias(self, professor, lista_materias):
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
        return sg.Window('Matérias', layout, finalize=True, size=(400, 400), element_justification='center')

    def iniciar_tela_materias(self, professor):
        lista_materias = self.controlador.obter_materias(professor)
        window = self.layout_tela_materias(professor, lista_materias)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            if event == 'Tabela':
                linha_clicada = values['Tabela'][0] if values['Tabela'] else None
                if linha_clicada is not None:
                    materia = lista_materias[linha_clicada]
                    self.iniciar_tela_materia(materia, professor)

        window.close()

    def layout_tela_turmas(self, professor, turmas):
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
        return sg.Window("Turmas", layout, finalize=True, size=(400, 400), element_justification='center')

    def iniciar_tela_turmas(self, professor):
        turmas = self.controlador.obter_turmas_professor(professor)
        window = self.layout_tela_turmas(professor, turmas)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            if event == 'Tabela':
                linha_clicada = values['Tabela'][0] if values['Tabela'] else None
                if linha_clicada is not None:
                    turma = turmas[linha_clicada]
                    self.iniciar_tela_alunos(turma)

            elif event == 'Voltar':
                window.close()
                return

        window.close()

    def layout_tela_materia(self, materia, professor):
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
             sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
             sg.Button('Adicionar Nota', key='ADICIONAR_NOTA', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0))),
             sg.Button('Ver Alunos', key='VER_ALUNOS', font=("Arial", 14), size=(15, 1), pad=((5, 5), (10, 0)))]
        ]
        return sg.Window("Matéria", layout, finalize=True, size=(500, 400), element_justification='center')

    def iniciar_tela_materia(self, materia, professor):
        window = self.layout_tela_materia(materia, professor)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            elif event == 'ADICIONAR_NOTA':
                self.iniciar_tela_adicionar_nota(materia)

            elif event == 'VER_ALUNOS':
                self.iniciar_tela_alunos(materia)

        window.close()

    def layout_tela_adicionar_nota(self, materia):
        layout = [
            [sg.Text('Adicionar Nota ou Prova', font=("Arial", 14))],
            [sg.Text('Tipo:', font=("Arial", 12)), sg.Combo(['Prova', 'Trabalho'], key='Tipo', size=(20, 1))],
            [sg.Text('Nome:', font=("Arial", 12)), sg.InputText(key='Nome', size=(20, 1))],
            [sg.Text('Nota:', font=("Arial", 12)), sg.InputText(key='Nota', size=(20, 1))],
            [sg.Button('Adicionar', font=("Arial", 14), size=(10, 1)),
             sg.Button('Cancelar', font=("Arial", 14), size=(10, 1))]
        ]
        return sg.Window('Adicionar Nota ou Prova', layout, finalize=True, size=(300, 200), element_justification='center')

    def iniciar_tela_adicionar_nota(self, materia):
        window = self.layout_tela_adicionar_nota(materia)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                break

            if event == 'Adicionar':
                tipo = values['Tipo']
                nome = values['Nome']
                nota = values['Nota']

                if tipo and nome and nota:
                    # Adicionar lógica para salvar a nota ou prova
                    print(f"Tipo: {tipo}, Nome: {nome}, Nota: {nota}")
                    # Atualize a matéria com a nova nota ou prova aqui
                else:
                    sg.popup_error('Todos os campos são obrigatórios.')

        window.close()

    def layout_tela_alunos(self, turma, lista_alunos):
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
        return sg.Window("Alunos", layout, finalize=True, size=(500, 400), element_justification='center')

    def iniciar_tela_alunos(self, turma):
        lista_alunos = self.controlador.obter_alunos_por_turma(turma)
        window = self.layout_tela_alunos(turma, lista_alunos)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            if event == 'Tabela':
                if values['Tabela']:  # Verifica se há uma linha selecionada
                    linha_clicada = values['Tabela'][0]  # Obtém a linha clicada
                    aluno = lista_alunos[linha_clicada]
                    self.iniciar_tela_atribuir_notas(aluno)

            elif event == 'Voltar':
                window.close()
                return


            window.close()

    def layout_tela_atribuir_notas(self, aluno):
        materias = self.controlador.obter_materias_do_aluno(aluno)  # Supondo que você tenha esse método

        layout = [
            [sg.Text(f"Atribuir nota para {aluno.nome}", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Text("Selecione a matéria:", font=("Arial", 14))],
            [sg.Combo([materia.nome for materia in materias], key="Materia", font=("Arial", 14), size=(30, 1))],
            [sg.Text("Nota:", font=("Arial", 14))],
            [sg.InputText(key="Nota", font=("Arial", 14), size=(30, 1))],
            [sg.Button('Salvar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
            sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]
        return sg.Window("Atribuir Nota", layout, finalize=True, size=(400, 300), element_justification='center')

    def iniciar_tela_atribuir_notas(self, aluno):
        window = self.layout_tela_atribuir_notas(aluno)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Voltar'):
                break

            if event == 'Salvar':
                materia_nome = values['Materia']
                nota = values['Nota']
                if materia_nome and nota:
                    try:
                        nota = float(nota)
                        self.controlador.atribuir_nota(aluno, materia_nome, nota)
                        sg.popup("Nota atribuída com sucesso!", title="Sucesso")
                    except ValueError:
                        sg.popup("Nota deve ser um número válido.", title="Erro")
                else:
                    sg.popup("Por favor, preencha todos os campos.", title="Erro")

        window.close()

