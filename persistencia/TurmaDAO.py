import json
from persistencia.BaseDAO import BaseDAO
from modelo.escola.Turma import Turma

class TurmaDAO(BaseDAO):
    def __init__(self, aluno_dao):
        super().__init__("turmas.json")
        self.aluno_dao = aluno_dao
        self.turmas = self.carregar_turmas()

    def carregar_turmas(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                dados = json.load(file)
        except FileNotFoundError:
            print("Arquivo de turmas não encontrado, criando novo arquivo.")
            dados = []
        except json.JSONDecodeError:
            print("Erro ao carregar turmas: arquivo JSON está malformado.")
            dados = []

        turmas = []
        for item in dados:
            turma = Turma(
                nome_turma=item['nome'],
                alunos=[self.aluno_dao.buscar_aluno(matricula) for matricula in item['alunos']],
                materias=item['materias']
            )
            turmas.append(turma)
        return turmas

    def salvar_turmas(self):
        dados = []
        for turma in self.turmas:
            dados.append({
                "nome": turma.nome_turma,
                "alunos": [aluno.matricula for aluno in turma.alunos],
                "materias": turma.materias
            })
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(dados, file, indent=4, ensure_ascii=False)

    def adicionar_turma(self, turma):
        self.turmas.append(turma)
        self.salvar_turmas()

    def remover_turma(self, nome_turma):
        self.turmas = [turma for turma in self.turmas if turma.nome_turma != nome_turma]
        self.salvar_turmas()

    def remover_turma_por_materia(self, nome_materia):
        turmas_iniciais = len(self.turmas)
        self.turmas = [turma for turma in self.turmas if nome_materia not in turma.materias]
        turmas_finais = len(self.turmas)
        if turmas_iniciais > turmas_finais:
            print(f"Turmas que tinham a matéria '{nome_materia}' foram removidas.")
        else:
            print(f"Nenhuma turma encontrada com a matéria '{nome_materia}'.")
        self.salvar_turmas()

    def buscar_turma(self, nome):
        for turma in self.turmas:
            if turma.nome_turma == nome:
                return turma
        return None

    def adicionar_aluno_em_turma(self, nome_turma, matricula):
        turma = self.buscar_turma(nome_turma)
        if turma:
            aluno = self.aluno_dao.buscar_aluno(matricula)
            if aluno and aluno not in turma.alunos:
                turma.alunos.append(aluno)
                self.salvar_turmas()
                print(f"Aluno {aluno.nome} adicionado à turma {nome_turma}.")
            else:
                print("Aluno não encontrado ou já está na turma.")
        else:
            print(f"Turma {nome_turma} não encontrada.")

    def remover_aluno_de_turma(self, nome_turma, matricula):
        turma = self.buscar_turma(nome_turma)
        if turma:
            aluno = self.aluno_dao.buscar_aluno(matricula)
            if aluno and aluno in turma.alunos:
                turma.alunos.remove(aluno)
                self.salvar_turmas()
            else:
                print("Aluno não encontrado na turma.")
        else:
            print(f"Turma {nome_turma} não encontrada.")

    def adicionar_materia_em_turma(self, nome_turma, nome_materia):
        turma = self.buscar_turma(nome_turma)
        if turma:
            if nome_materia not in turma.materias:
                turma.materias.append(nome_materia)
                self.salvar_turmas()
                print(f"Matéria '{nome_materia}' adicionada à turma '{nome_turma}'.")
            else:
                print("Matéria já está na turma.")
        else:
            print(f"Turma '{nome_turma}' não encontrada.")

    def remover_materia_de_turma(self, nome_turma, nome_materia):
        turma = self.buscar_turma(nome_turma)
        if turma:
            if nome_materia in turma.materias:
                turma.materias.remove(nome_materia)
                self.salvar_turmas()
                print(f"Matéria '{nome_materia}' removida da turma '{nome_turma}'.")
            else:
                print("Matéria não encontrada na turma.")
        else:
            print(f"Turma '{nome_turma}' não encontrada.")

    def buscar_turmas(self):
        return self.turmas

    def imprimir_tudo(self):
        for turma in self.turmas:
            print(turma)
            print("-" * 40)
