import json
from modelo.escola.Turma import Turma

CAMINHO = "persistencia/dados/"

class TurmaDAO:
    def __init__(self, aluno_dao):
        self.turmas = {}
        self.aluno_dao = aluno_dao
        self.carregar_turmas()

    def salvar_turmas(self):
        turmas_data = [
            {
                "nome": turma.nome_turma,
                "alunos": [aluno.matricula for aluno in turma.alunos],
                "materias": [materia.nome for materia in turma.materias]
            }
            for turma in self.turmas.values()
        ]
        with open(CAMINHO + "turmas.json", "w", encoding="utf-8") as arquivo:
            json.dump(turmas_data, arquivo, indent=4, ensure_ascii=False)

    def carregar_turmas(self):
        try:
            with open(CAMINHO + "turmas.json", 'r', encoding='utf-8') as arquivo:
                turmas_data = json.load(arquivo)
                for dados in turmas_data:
                    alunos = [self.aluno_dao.buscar_aluno(matricula) for matricula in dados['alunos']]
                    turma = Turma(dados['nome'])
                    turma.alunos = [aluno for aluno in alunos if aluno is not None]
                    # A atribuição de matérias pode ser realizada em outro momento ou através de outro método
                    self.turmas[turma.nome_turma] = turma
        except FileNotFoundError:
            pass

    def adicionar_turma(self, turma):
        self.turmas[turma.nome_turma] = turma
        self.salvar_turmas()

    def remover_turma(self, nome_turma):
        if nome_turma in self.turmas:
            del self.turmas[nome_turma]
            self.salvar_turmas()

    def buscar_turma(self, nome_turma):
        return self.turmas.get(nome_turma)
