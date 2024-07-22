import json
from persistencia.dados import Escola
class Gravador:
    def __init__(self, escola: Escola):
        self.escola = escola

    def gravar_professores(self, caminho):
        lista_professores = []

        for professor in self.escola.Professores.values():
            dados_professor = {
                "nome": professor.nome,
                "idade": professor.idade,
                "email": professor.email,
                "registro": professor.registro,
                "salario": professor.salario
            }
            lista_professores.append(dados_professor)
        with open(caminho, "w") as arquivo:
            json.dump(lista_professores, arquivo, indent=4)
    def gravar_alunos(self, caminho):
        lista_alunos = []

        for aluno in self.escola.Alunos.values():
            dados_aluno = {
                "nome": aluno.nome,
                "idade": aluno.idade,
                "email": aluno.email,
                "matricula": aluno.matricula,
                "turma": aluno.turma.nome_turma,
                "notas": {str(materia.nome): nota for materia, nota in aluno.notas.items()}  # Convertendo as chaves para strings
            }
            lista_alunos.append(dados_aluno)
        with open(caminho, "w") as arquivo:
            json.dump(lista_alunos, arquivo, indent=4)
    def gravar_secretarios(self, caminho):
        lista_secretarios = []
        for secretario in self.escola.Secretarios.values():
            dados_secretario = {
                "nome": secretario.nome,
                "idade": secretario.idade,
                "email": secretario.email,
                "registro": secretario.registro,
                "salario": secretario.salario
            }
            lista_secretarios.append(dados_secretario)

        with open(caminho, "w") as arquivo:
                json.dump(lista_secretarios, arquivo, indent=4)
