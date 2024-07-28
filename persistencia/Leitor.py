import json
from persistencia import Escola
from modelo.escola import Materia


CAMINHO = "persistencia/dados/"

class Leitor():
    def __init__(self, escola: Escola):
        self.escola = escola

    def lista_secretarios(self):
        with open(CAMINHO + "secretarios.json", 'r', encoding='utf-8') as arquivo:
            secretarios = json.load(arquivo)
            for secretario in secretarios:
                self.escola.add_secretario(
                    secretario['nome'],
                    secretario['idade'],
                    secretario['email'],
                    secretario['registro'],
                    secretario['salario']
                )

    def lista_professores(self):  # Funcionando
        with open(CAMINHO + "professores.json", 'r', encoding='utf-8') as arquivo:
            professores = json.load(arquivo)
            for professor in professores:
                self.escola.add_professor(
                    professor['nome'],
                    professor['idade'],
                    professor['email'],
                    professor['registro'],
                    professor['salario']
                )

    def lista_alunos(self):
        with open(CAMINHO + "alunos.json", 'r', encoding='utf-8') as arquivo:
            alunos = json.load(arquivo)
            for aluno in alunos:
                self.escola.add_aluno(
                    aluno['nome'],
                    aluno['idade'],
                    aluno['email'],
                    aluno['matricula'],
                    aluno['turma'],
                    aluno['notas']
                )
                
    def lista_materias(self):
        with open(CAMINHO + "materias.json", 'r', encoding='utf-8') as arquivo:
            materias = json.load(arquivo)
            for materia in materias:
                professor = self.escola.get_professor_por_nome(materia['professor'])
                if professor:
                    nova_materia = Materia(materia['nome'], professor, materia['turma'])
                    nova_materia.provas = materia.get('provas', {})
                    nova_materia.trabalhos = materia.get('trabalhos', {})
                    self.escola.add_materia(nova_materia)

    def testar_senha(self, registro, senha):
        with open(CAMINHO + "registros.json", 'r', encoding='utf-8') as arquivo:
            registros = json.load(arquivo)
            for reg in registros:
                if registro == reg['registro'] and senha == reg['senha']:
                    return reg['tipo']
                
        return "N"

