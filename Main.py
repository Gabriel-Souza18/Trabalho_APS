from modelo.pessoas import *
from modelo.escola import *
from persistencia import Escola, Gravador, Leitor

from visao.telaInicialAluno import *
from visao.telaLogin import *

def main():
    escola = Escola("Escola Estadual")

    carregarDados(escola)

    telaLogin(escola) # Funcionando!
    #salvarDados(escola)


def carregarDados(escola):
    leitor = Leitor(escola)
    leitor.lista_professores()
    leitor.lista_secretarios()
    leitor.lista_alunos()
    leitor.lista_materias()

    escola.imprimir_tudo()


def salvarDados(escola):
    gravador = Gravador(escola)
    gravador.gravar_secretarios()
    gravador.gravar_alunos()
    gravador.gravar_professores()
    gravador.gravar_materias()

if __name__ == "__main__":
    main()
