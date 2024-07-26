from modelo.pessoas import *
from modelo.escola import *
from persistencia import Escola, Gravador, Leitor

from visao.telaInicialAluno import *
from visao.telaLogin import *

CAMINHO = "persistencia/dados/"

def main():
    escola = Escola("Escola Estadual")
    diretor = Secretario("Matheus Viana", 50, "MatheusV@hotmail.com", 202254, 4500.00)

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
    gravador.gravar_secretarios(CAMINHO + "secretarios.txt")
    gravador.gravar_alunos(CAMINHO + "alunos.txt")
    gravador.gravar_professores(CAMINHO + "professores.txt")

    # Funcionando!

    leitor = Leitor(escola)
    leitor.lista_professores()
    leitor.lista_secretarios()
    leitor.lista_alunos()

    # Funcionando!

    registro = telaLogin(escola) # Funcionando!
    #TelaInicial(aluno, turma)

if __name__ == "__main__":
    main()
