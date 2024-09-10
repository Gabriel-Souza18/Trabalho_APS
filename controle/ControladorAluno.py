import PySimpleGUI as sg
from visao.telaInicialAluno import (
    layout_tela_inicial_aluno,
    layout_tela_notas,
    layout_tela_turma,
    layout_tela_materia
)

class ControladorTelaInicialAluno:
    def __init__(self, aluno_dao, turma_dao, materia_dao):
        self.aluno_dao = aluno_dao
        self.turma_dao = turma_dao
        self.materia_dao = materia_dao

    def iniciar_tela_inicial_aluno(self, aluno, turma):
        window = layout_tela_inicial_aluno(aluno, turma)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == 'NOTAS':
                self.iniciar_tela_notas(aluno)

            elif event == 'TURMA':
                self.iniciar_tela_turma(turma)

        window.close()

    def iniciar_tela_notas(self, aluno):
        window = layout_tela_notas(aluno, self.materia_dao)  # Ajuste para passar materia_dao

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break

            elif event == 'Voltar':
                window.close()
                return

            elif event == 'Tabela':
                if values['Tabela']:
                    linha_clicada = values['Tabela'][0]
                    nome_materia = window['Tabela'].get()[linha_clicada][0]
                    materia = self.materia_dao.buscar_materia_por_nome(nome_materia)
                    self.iniciar_tela_materia(materia, aluno.notas.get(nome_materia, {}))

        window.close()

    def iniciar_tela_turma(self, turma):
        window = layout_tela_turma(turma)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Fechar':
                break

            elif event == 'Voltar':
                window.close()
                return

        window.close()

    def iniciar_tela_materia(self, materia, notas_aluno):
        window = layout_tela_materia(materia, notas_aluno)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'FECHAR':
                break

            elif event == 'Voltar':
                window.close()
                return

        window.close()