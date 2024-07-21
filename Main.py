from modelo.pessoas import *
from modelo.escola import *
from persistencia.dados import Escola, Gravador

from visao.telaInicialAluno import *


def main():
    escola = Escola("Escola Estadual")
    diretor = Secretario("Secretario", 50, "secretario@hotmail.com", 202254, 4500.00)

    gabriel = Professor("Gabriel", 28, "Gabriel@gmail.com", 202251, 2500.00)
    gustavo = Professor("Gustavo", 30, "Gustavo@gmail.com", 202253, 2000.00)

    geografia = Materia("Geografia", gabriel)
    portugues = Materia("Português", gustavo)

    turma = Turma("7° ano A")
    turma.materias.append(geografia)
    turma.materias.append(portugues)

    aluno = Aluno("Braian", 20, "Braian@gmail.com", 202202, turma, {geografia: 8, portugues: 7})
    turma.alunos.append(aluno)

    # testes com gravador e leitor
    escola.add_aluno(aluno)
    escola.add_professor(gabriel)
    escola.add_professor(gustavo)
    escola.add_secretario(diretor)

    gravador = Gravador(escola)
    gravador.gravar_secretarios("secretarios.txt")
    gravador.gravar_alunos("alunos.txt")
    gravador.gravar_professores("professores.txt")

    # Funcionou!

    # TelaInicial(aluno, turma)


if __name__ == "__main__":
    main()
