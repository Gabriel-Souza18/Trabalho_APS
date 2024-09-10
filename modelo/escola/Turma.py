class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.alunos = []          # Lista de objetos Aluno
        self.materias = []        # Lista de objetos Materia

    def __str__(self):
        return f"Turma(nome_turma={self.nome_turma}, alunos={len(self.alunos)}, materias={len(self.materias)})"

    __repr__ = __str__
