from modelo.pessoas import Secretario, Professor, Aluno
from modelo.escola import Materia, Turma

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.Secretarios = {}
        self.Professores = {}
        self.Alunos = {}
        self.Materias = {}
        self.Turmas = {}

    def add_secretario(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], Secretario):
            secretario = args[0]
            self.Secretarios[secretario.registro] = secretario
        elif len(args) == 5:
            nome, idade, email, registro, salario = args
            novo_secretario = Secretario(nome, idade, email, registro, salario)
            self.Secretarios[novo_secretario.registro] = novo_secretario
        else:
            raise ValueError("Número incorreto de argumentos!")

    def add_professor(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], Professor):
            professor = args[0]
            self.Professores[professor.registro] = professor
        elif len(args) == 5:
            nome, idade, email, registro, salario = args
            novo_professor = Professor(nome, idade, email, registro, salario)
            self.Professores[novo_professor.registro] = novo_professor
        else:
            raise ValueError("Número incorreto de argumentos!")

    def add_aluno(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], Aluno):
            aluno = args[0]
            self.Alunos[aluno.matricula] = aluno
        elif len(args) == 6:
            nome, idade, email, matricula, turma, notas = args
            novo_aluno = Aluno(nome, idade, email, matricula, turma, notas)
            self.Alunos[novo_aluno.matricula] = novo_aluno
            if turma not in self.Turmas:
                self.Turmas[turma] = Turma(turma)
            self.Turmas[turma].alunos.append(novo_aluno)
        else:
            raise ValueError("Número incorreto de argumentos!")

    def add_materia(self, materia):
        self.Materias[materia.nome] = materia
        if materia.turma not in self.Turmas:
            self.Turmas[materia.turma] = Turma(materia.turma)
        self.Turmas[materia.turma].materias.append(materia)

    def get_secretario(self, registro):
        return self.Secretarios.get(registro, None)

    def get_professor(self, registro):
        return self.Professores.get(registro, None)

    def get_professor_por_nome(self, nome):
        for professor in self.Professores.values():
            if professor.nome == nome:
                return professor
        return None

    def get_aluno(self, registro):
        return self.Alunos.get(registro, None)

    def get_turma_do_aluno(self, aluno):
        for turma in self.Turmas.values():
            if aluno in turma.alunos:
                return turma
        return None

    def get_materia_por_nome(self, nome_materia):
        for materia in self.Materias.values():
            if materia.nome == nome_materia:
                return materia
        return None

    def imprimir_tudo(self):
        print("Secretarios:")
        for secretario in self.Secretarios.values():
            print(secretario)

        print("\nProfessores:")
        for professor in self.Professores.values():
            print(professor)

        print("\nAlunos:")
        for aluno in self.Alunos.values():
            print(aluno)

        print("\nMaterias:")
        for materia in self.Materias.values():
            print(f"Nome: {materia.nome}, Professor: {materia.professor.nome}, Turma: {materia.turma}")
            print("  Provas:")
            for prova, nota in materia.provas.items():
                print(f"    {prova}: {nota}")
            print("  Trabalhos:")
            for trabalho, nota in materia.trabalhos.items():
                print(f"    {trabalho}: {nota}")

        print("\nTurmas:")
        for turma in self.Turmas.values():
            print(turma)

