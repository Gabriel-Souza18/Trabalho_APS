import json
from modelo.pessoas.Aluno import Aluno  # Supondo que o modelo do Aluno está nesse caminho

CAMINHO = "persistencia/dados/"

class AlunoDAO:
    def __init__(self):
        self.alunos = {}  # Dicionário para armazenar alunos com matrícula como chave
        self.carregar_alunos()  # Carrega os alunos no início

    def salvar_alunos(self):
        alunos_data = [
            {
                "nome": aluno.nome,
                "idade": aluno.idade,
                "email": aluno.email,
                "matricula": aluno.matricula,
                "turma": aluno.turma,
                "notas": aluno.notas
            }
            for aluno in self.alunos.values()
        ]
        with open(CAMINHO + "alunos.json", "w", encoding="utf-8") as arquivo:
            json.dump(alunos_data, arquivo, indent=4, ensure_ascii=False)

    def carregar_alunos(self):
        try:
            with open(CAMINHO + "alunos.json", 'r', encoding='utf-8') as arquivo:
                alunos_data = json.load(arquivo)
                for dados in alunos_data:
                    aluno = Aluno(
                        dados['nome'],
                        dados['idade'],
                        dados['email'],
                        dados['matricula'],
                        dados['turma'],
                        dados['notas']
                    )
                    self.alunos[aluno.matricula] = aluno
        except FileNotFoundError:
            pass

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos[aluno.matricula] = aluno
        self.salvar_alunos()

    def remover_aluno(self, matricula):
        if matricula in self.alunos:
            del self.alunos[matricula]
            self.salvar_alunos()

    def buscar_aluno(self, matricula):
        return self.alunos.get(matricula)
