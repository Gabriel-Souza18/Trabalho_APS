from src.escola import Escola
from src.interface import TelaLogin
from src.pessoas import Professor, Secretario


def main():
    escola_fundamental = Escola(nome="Escola Fundamental")

    jose_secretario = Secretario("Jose", 45, 1234, "jose@email.com", escola_fundamental)
    mario_secretario = Secretario("Mario", 50, 4321, "mario@email.com", escola_fundamental)

    # escola.adicionar_secretario(jose_secretario)
    # escola.adicionar_secretario(mario_secretario)

    jorge_professor = Professor("Jorge", 26, 7410, 1200.00, "jorge@gmail.com")

    jose_secretario.ler_turma("Turma1")
    jose_secretario.ler_turma("Turma2")

    tela_login = TelaLogin(escola_fundamental)

    tela_login.cadastrar_usuario(usuario=jose_secretario, senha="SenhaForte")
    tela_login.cadastrar_usuario(usuario=mario_secretario, senha="SenhaFraca")
    tela_login.cadastrar_usuario(usuario=jorge_professor, senha="teste")

    tela_login.show_tela_login()


main()
