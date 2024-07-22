from modelo.pessoas import *
from modelo.escola import *
from persistencia.dados import Escola, Gravador, Leitor

from visao.telaInicialAluno import *


def main():
    escola = Escola("Escola Estadual")
    turma = Turma("7 ano A")
    escola.Turmas.append(turma)
    # testes com leitor
    leitor = Leitor(escola)
    leitor.lista_professores("professores.Json")
    leitor.lista_secretarios("secretarios.Json")
    leitor.lista_alunos("alunos.Json")

    geografia = Materia("Geografia", escola.Professores[202251])
    portugues = Materia("Portugues", escola.Professores[202253])



    turma.materias.append(geografia)
    turma.materias.append(portugues)



    # com o Leitor nao precisa iniciar tudo denovo

    '''diretor = Secretario("Secretario", 50, "secretario@hotmail.com", 202254, 4500.00)

    gabriel = Professor("Gabriel", 28, "Gabriel@gmail.com", 202251, 2500.00)
    gustavo = Professor("Gustavo", 30, "Gustavo@gmail.com", 202253, 2000.00)

    geografia = Materia("Geografia", gabriel)
    portugues = Materia("Portugues", gustavo)

    geografia = Materia("Geografia", gabriel)
    portugues = Materia("Portugues", gustavo)

    turma.materias.append(geografia)
    turma.materias.append(portugues)
    escola.add_professor(gabriel)
    escola.add_professor(gustavo)
    escola.add_secretario(diretor)

    teste = Aluno("Teste2", 21, "teste@gmail.com", 152123, turma, {geografia: 4, portugues: 9})
    Braian = Aluno("Braian", 20, "Braian@gmail.com", 202202, turma, {geografia: 8, portugues: 7})
    turma.alunos.append(teste)
    turma.alunos.append(Braian)
    escola.add_aluno(teste)
    escola.add_aluno(Braian)'''


    escola.imprimir_escola()
    # testes com gravador
    gravador = Gravador(escola)
    gravador.gravar_secretarios("secretarios.Json")
    gravador.gravar_professores("professores.Json")
    gravador.gravar_alunos("alunos.Json")

    # Funcionou!

    TelaInicial(escola.Alunos[202202], turma)


if __name__ == "__main__":
    main()
