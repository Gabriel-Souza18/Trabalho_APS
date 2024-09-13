class Materia:
    def __init__(self, nome, professor, turma, provas=None, trabalhos=None):
        self.nome = nome
        self.professor = professor
        self.turma = turma
        self.provas = provas if provas is not None else {}
        self.trabalhos = trabalhos if trabalhos is not None else {}

    def __str__(self):
        provas_str = "\n".join([f"  {nome}: {nota}" for nome, nota in self.provas.items()]) or "Nenhuma prova registrada"
        trabalhos_str = "\n".join([f"  {nome}: {nota}" for nome, nota in self.trabalhos.items()]) or "Nenhum trabalho registrado"
        
        return (f"Nome: {self.nome}\n"
                f"Professor: {self.professor}\n"
                f"Turma: {self.turma}\n"
                f"Provas:\n{provas_str}\n"
                f"Trabalhos:\n{trabalhos_str}")

    __repr__ = __str__
