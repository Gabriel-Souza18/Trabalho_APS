import json
from persistencia import Escola
from persistencia import Leitor


class Gravador:


    def __init__(self, escola: Escola):
        self.escola = escola

    def gravar_professores(self):
        professores = [
            {
                "nome": professor.nome,
                "idade": professor.idade,
                "email": professor.email,
                "registro": professor.registro,
                "salario": professor.salario
            }
            for professor in self.escola.Professores.values()
        ]
        with open(Leitor.CAMINHO + "professores.json", "w", encoding="utf-8") as arquivo:
            json.dump(professores, arquivo, indent=4, ensure_ascii=False)

    def gravar_alunos(self):
        alunos = [
            {
                "nome": aluno.nome,
                "idade": aluno.idade,
                "email": aluno.email,
                "matricula": aluno.matricula,
                "turma": aluno.turma,
                "notas": aluno.notas
            }
            for aluno in self.escola.Alunos.values()
        ]
        with open(Leitor.CAMINHO  + "alunos.json", "w", encoding="utf-8") as arquivo:
            json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

    def gravar_secretarios(self):
        secretarios = [
            {
                "nome": secretario.nome,
                "idade": secretario.idade,
                "email": secretario.email,
                "registro": secretario.registro,
                "salario": secretario.salario
            }
            for secretario in self.escola.Secretarios.values()
        ]
        with open(Leitor.CAMINHO + "secretarios.json", "w", encoding="utf-8") as arquivo:
            json.dump(secretarios, arquivo, indent=4, ensure_ascii=False)

    def gravar_materias(self):
        materias = [
            {
                "nome": materia.nome,
                "professor": materia.professor.nome,
                "turma": materia.turma,
                "provas": materia.provas,
                "trabalhos": materia.trabalhos
            }
            for materia in self.escola.Materias.values()
        ]
        with open(Leitor.CAMINHO + "materias.json", "w", encoding="utf-8") as arquivo:
            json.dump(materias, arquivo, indent=4, ensure_ascii=False)

