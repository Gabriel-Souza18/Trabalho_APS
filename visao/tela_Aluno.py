import PySimpleGUI as sg

class TelaAluno:
    def __init__(self, controlador):
        self.controlador = controlador

    def tela_aluno(self, aluno, turma):
        sg.theme('DarkBlue12')
        layout = [
            [sg.Text(f'Nome: {aluno.nome}', font=("Arial", 14)),
             sg.Text('', size=(15, 1)),
             sg.Text(f'Matrícula: {aluno.matricula}', font=("Arial", 14))],
            [sg.Text(f'Email: {aluno.email}', font=("Arial", 14))],
            [sg.Button("Ver Notas", key="NOTAS", size=(15, 1), font=("Arial", 14)),
             sg.Button("Ver Turma", key="TURMA", size=(15, 1), font=("Arial", 14))]
        ]

        window = sg.Window("Tela Inicial do Aluno", layout, size=(450, 150), element_justification='center', finalize=True)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == 'NOTAS':
                lista_materias = self.controlador.obter_materias(aluno)
                self.tela_notas(aluno, lista_materias)

            elif event == 'TURMA':
                alunos = self.controlador.obter_alunos_turma(turma)
                self.tela_turma(turma, alunos)

        window.close()

    def tela_notas(self, aluno, lista_materias):
        linhas_tabela = []
        for materia_nome, notas in aluno.notas.items():
            materia = next((m for m in lista_materias if m.nome == materia_nome), None)
            if not materia:
                continue

            if not hasattr(materia, 'provas') or not hasattr(materia, 'trabalhos'):
                continue

            if isinstance(materia.provas, dict) and isinstance(materia.trabalhos, dict):
                nota_total = sum(notas.get('provas', {}).values()) + sum(notas.get('trabalhos', {}).values())
                nota_maxima = sum(materia.provas.values()) + sum(materia.trabalhos.values())
                percentual = (nota_total / nota_maxima * 100) if nota_maxima > 0 else 0
                linhas_tabela.append([materia_nome, f"{nota_total:.2f}", f"{nota_maxima:.2f}", f"{percentual:.2f}%"])

        linhas_tabela.sort(key=lambda x: x[0])

        layout = [
            [sg.Text("Clique na matéria para ver detalhes", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Table(values=linhas_tabela,
                      headings=["Matéria", "Nota", "N. distribuída", "Percentual"],
                      key="Tabela",
                      auto_size_columns=False,
                      col_widths=[10, 10, 10, 10],
                      justification='center',
                      enable_events=True,
                      font=("Arial", 14),
                      row_height=25)],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
             sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]

        window = sg.Window('Notas', layout, finalize=True, size=(700, 400), element_justification='center')


        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            if event == 'Tabela':
                linha_clicada = values['Tabela'][0] if values['Tabela'] else None
                if linha_clicada is not None:
                    materia = lista_materias[linha_clicada]
                    self.tela_materia(materia, aluno.notas.get(materia.nome, {}))

        window.close()

    def tela_turma(self, turma, alunos):
        linhas_tabela = [[aluno.matricula, aluno.nome, aluno.idade] for aluno in alunos if aluno is not None]
        linhas_tabela.sort(key=lambda x: x[1])

        layout = [
            [sg.Text(f"Turma: {turma.nome_turma}", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Table(values=linhas_tabela,
                      headings=["Matrícula", "Nome", "Idade"],
                      key="Tabela",
                      auto_size_columns=False,
                      col_widths=[10, 20, 10],
                      justification='center',
                      display_row_numbers=True,
                      font=("Arial", 14),
                      row_height=25)],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
             sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]

        window = sg.Window("Turma", layout, finalize=True, size=(450, 400), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            elif event == 'Voltar':
                window.close()
                return

        window.close()

    def tela_materia(self, materia, notas_aluno):
        dados_arvore = sg.TreeData()

        dados_arvore.insert("", "CP", "Provas", [('')])
        for prova, valor in materia.provas.items():
            nota_aluno = notas_aluno.get('provas', {}).get(prova, '')
            dados_arvore.insert("CP", prova, prova, [f"{nota_aluno} : {valor}"])

        dados_arvore.insert("", "CT", "Trabalhos", [('')])
        for trabalho, valor in materia.trabalhos.items():
            nota_aluno = notas_aluno.get('trabalhos', {}).get(trabalho, '')
            dados_arvore.insert("CT", trabalho, trabalho, [f"{nota_aluno} : {valor}"])

        professor_nome = materia.professor.nome if materia.professor else "Desconhecido"

        layout = [
            [sg.Text(f"{materia.nome} - Professor: {professor_nome}", font=("Arial", 14), pad=((0, 0), (10, 10)))],
            [sg.Tree(data=dados_arvore,
                     headings=["Valor"],
                     key="Arvore",
                     auto_size_columns=False,
                     col_widths=[30],
                     justification='center',
                     font=("Arial", 14),
                     row_height=25)],
            [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
             sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
        ]

        window = sg.Window("Matéria", layout, finalize=True, size=(500, 300), element_justification='center')

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                break

            elif event == 'Voltar':
                window.close()
                return

        window.close()
