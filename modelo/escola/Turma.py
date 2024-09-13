class Turma:
    def __init__(self, nome_turma, alunos=None, materias=None):
        self.nome_turma = nome_turma
        self.alunos = alunos if alunos is not None else [] 
        self.materias = materias if materias is not None else [] 

    def __str__(self):
        return f"Turma(nome_turma={self.nome_turma}, alunos={len(self.alunos)}, materias={len(self.materias)})"

    __repr__ = __str__
