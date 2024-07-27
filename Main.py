from modelo.pessoas import *
from modelo.escola import *
from persistencia import Escola, Gravador, Leitor

from visao.telaInicialAluno import *
from visao.telaLogin import *

CAMINHO = "persistencia/dados/"

def main():
    escola = Escola("Escola Estadual")
    diretor = Secretario("Matheus Viana", 50, "MatheusV@hotmail.com", 202254, 4500.00)

    turma7A = Turma("7 ano A")
    turma7B = Turma("7 ano B")
    escola.Turmas.append(turma7A)
    escola.Turmas.append(turma7B)

    leitor = Leitor(escola)

    leitor.lista_professores(CAMINHO + "professores.Json")
    leitor.lista_secretarios(CAMINHO + "secretarios.Json")
    leitor.lista_alunos(CAMINHO + "alunos.Json")
    escola.organizar_alunos()

    geografia = Materia("Geografia", escola.Professores[202251])
    portugues = Materia("Português", escola.Professores[202253])

    turma7A.materias.append(geografia)
    turma7A.materias.append(portugues)

    turma7B.materias.append(geografia)
    turma7B.materias.append(portugues)

    gabriel = Professor("Gabriel", 28, "Gabriel@gmail.com", 202251, 2500.00)
    gustavo = Professor("Gustavo", 30, "Gustavo@gmail.com", 202253, 2000.00)
    aluno = Aluno("Braian", 20, "Braian@gmail.com", 202202, turma7A)
    
    turma7A.alunos.append(aluno)
    
    #testes com gravador e leitor
    escola.add_aluno(aluno)
    escola.add_professor(gabriel)
    escola.add_professor(gustavo)
    escola.add_secretario(diretor)

    gravador = Gravador(escola)
    gravador.gravar_materia(CAMINHO, geografia)
    gravador.gravar_secretarios(CAMINHO + "secretarios.Json")
    gravador.gravar_alunos(CAMINHO + "alunos.Json")
    gravador.gravar_professores(CAMINHO + "professores.Json")

    # Funcionando!


    # Funcionando!
    escola.imprimir_escola()
    escola.Alunos[202202].imprimir()

    registro = telaLogin(escola) # Funcionando!
    print("\n",registro)
    #TelaInicial(aluno, turma)

if __name__ == "__main__":
    main()
