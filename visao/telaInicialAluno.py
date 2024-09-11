import PySimpleGUI as sg


def layout_tela_inicial_aluno(aluno, turma):
    sg.theme('DarkBlue12')

    layout = [
        [sg.Text(f'Nome: {aluno.nome}', font=("Arial", 14)), sg.Text('', size=(15, 1)),
         sg.Text(f'Matrícula: {aluno.matricula}', font=("Arial", 14))],
        [sg.Text(f'Email: {aluno.email}', font=("Arial", 14))],
        [sg.Button("Ver Notas", key="NOTAS", size=(15, 1), font=("Arial", 14)),
         sg.Button("Ver Turma", key="TURMA", size=(15, 1), font=("Arial", 14))]
    ]
    return sg.Window("Tela Inicial do Aluno", layout, size=(450, 150), element_justification='center', finalize=True)


def layout_tela_notas(aluno, materia_dao):
    linhas_tabela = []
    for materia_nome, notas in aluno.notas.items():
        materia = materia_dao.buscar_materia_por_nome(materia_nome)
        if materia is None:
            continue  # Se a matéria não for encontrada, pule para a próxima

        nota_total = sum(notas.get('provas', {}).values()) + sum(notas.get('trabalhos', {}).values())
        nota_maxima = sum(materia.provas.values()) + sum(materia.trabalhos.values())
        percentual = (nota_total / nota_maxima * 100) if nota_maxima > 0 else 0
        linhas_tabela.append([materia_nome, f"{nota_total:.2f}", f"{nota_maxima:.2f}", f"{percentual:.2f}%"])

    linhas_tabela.sort(key=lambda x: x[0])

    layout = [
        [sg.Text("Clique na matéria para ver detalhes", font=("Arial", 14), pad=((0, 0), (10, 10)))],
        [sg.Table(values=linhas_tabela,
                  headings=["Matéria", "Nota Total", "Nota Máxima", "Percentual"],
                  key="Tabela",
                  auto_size_columns=False,
                  col_widths=[20, 15, 15, 15],
                  justification='center',
                  enable_events=True,
                  font=("Arial", 14),
                  row_height=25)],
        [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('Fechar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]
    return sg.Window('Notas', layout, finalize=True, size=(700, 400), element_justification='center')


def layout_tela_turma(turma):
    linhas_tabela = []
    for aluno in turma.alunos:
        linhas_tabela.append([aluno.matricula, aluno.nome, aluno.idade])

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
    return sg.Window("Turma", layout, finalize=True, size=(450, 400), element_justification='center')


def layout_tela_materia(materia, notas_aluno):
    dados_arvore = sg.TreeData()

    dados_arvore.insert("", "CP", "Provas", [('')])
    for prova, valor in materia.provas.items():
        nota_aluno = notas_aluno.get('provas', {}).get(prova, '')
        dados_arvore.insert("CP", prova, prova, [f"{nota_aluno} / {valor}"])

    dados_arvore.insert("", "CT", "Trabalhos", [('')])
    for trabalho, valor in materia.trabalhos.items():
        nota_aluno = notas_aluno.get('trabalhos', {}).get(trabalho, '')
        dados_arvore.insert("CT", trabalho, trabalho, [f"{nota_aluno} / {valor}"])

    layout = [
        [sg.Text(f"{materia.nome} - Professor: {materia.professor.nome}", font=("Arial", 14), pad=((0, 0), (10, 10)))],
        [sg.Tree(data=dados_arvore,
                 headings=["Valor", "Nota do Aluno"],
                 key="Arvore",
                 auto_size_columns=False,
                 col_widths=[30, 20],
                 justification='center',
                 font=("Arial", 14),
                 row_height=25)],
        [sg.Button('Voltar', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0))),
         sg.Button('FECHAR', font=("Arial", 14), size=(10, 1), pad=((5, 5), (10, 0)))]
    ]
    return sg.Window("Matéria", layout, finalize=True, size=(500, 300), element_justification='center')
