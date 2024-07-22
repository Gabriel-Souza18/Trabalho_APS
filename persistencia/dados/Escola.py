from modelo.pessoas import Secretario, Professor, Aluno


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.Secretarios = {}
        self.Professores = {}
        self.Alunos = {}
        self.Turmas = []

    def add_secretario(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], Secretario):
            # Se for passado um objeto Secretario, adiciona diretamente
            secretario = args[0]
            self.Secretarios[secretario.registro] = secretario
        elif len(args) == 5:
            # Se forem passados atributos individuais, cria um novo secretário
            nome, idade, email, registro, salario = args

            novo_secretario = Secretario(nome, idade, email, registro, salario)
            self.Secretarios[novo_secretario.registro] = novo_secretario
        else:
            raise ValueError("Número incorreto de argumentos!")

    def add_professor(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], Professor):
            # Se for passado um objeto Professor, adiciona diretamente
            professor = args[0]
            self.Professores[professor.registro] = professor
        elif len(args) == 5:
            # Se forem passados atributos individuais, cria um novo professor
            nome, idade, email, registro, salario = args

            novo_professor = Professor(nome, idade, email, registro, salario)
            self.Professores[novo_professor.registro] = novo_professor
        else:
            raise ValueError("Número incorreto de argumentos!")

    def add_aluno(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], Aluno):
            # Se for passado um objeto Aluno, adiciona diretamente
            aluno = args[0]
            self.Alunos[aluno.matricula] = aluno
        elif len(args) == 6:
            # Se forem passados atributos individuais, cria um novo aluno
            nome, idade, email, matricula, turma, notas = args
            notas = kwargs.get('notas', {})
            novo_aluno = Aluno(nome, idade, email, matricula, turma, notas)
            self.Alunos[novo_aluno.matricula] = novo_aluno
        else:
            raise ValueError("Número incorreto de argumentos!")

    def imprimir_escola(self):
        print("-----Alunos-----")
        for aluno in self.Alunos.values():
            print(aluno.nome)
        print("-----Professores----- ")
        for professor in self.Professores.values():
            print(professor.nome)
        print("-----Secretarios-----")
        for secretario in self.Secretarios.values():
            print(secretario.nome)
