from persistencia import Escola


class Gravador:
    def __init__(self, escola: Escola):
        self.escola = escola

    def gravar_professores(self, caminho):
        arquivo = open(caminho, "w")
        for professor in self.escola.Professores.values():
            arquivo.write(f"{professor.nome}/ {professor.idade}/ {professor.email}/ {professor.registro}/ {professor.salario}\n")

    def gravar_alunos(self, caminho):
        arquivo = open(caminho, "w")
        for aluno in self.escola.Alunos.values():
            arquivo.write(f"{aluno.nome}/ {aluno.idade}/ {aluno.matricula}/")

            for materia,nota in aluno.notas.items():
                arquivo.write(f" {materia.nome}:{nota}/")

            arquivo.write(f" {aluno.turma.nome_turma}/ {aluno.email}\n")

                          

    def gravar_secretarios(self, caminho):
        with open(caminho, "w") as arquivo:
            for secretario in self.escola.Secretarios.values():
                linha = f"{secretario.nome}/ {secretario.idade}/ {secretario.email}/ {secretario.registro}/ {secretario.salario}\n"
                arquivo.write(linha)
