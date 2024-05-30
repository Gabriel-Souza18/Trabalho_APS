from pessoas import *
from escola import*
from interface import*


def main():
    escola = Escola(nome="Escola Fundamental")

    jose_secretario = Secretario("Jose", 45, 1234, "jose@email.com", escola)
    mario_secretario = Secretario("Mario", 50, 4321, "mario@email.com",escola)

    jorge_professor = Professor("Jorge", 26, 7410,1200.00,"jorge@gmail.com")

    escola.adicionar_turma(jose_secretario.ler_turma("Turma1"))
    escola.adicionar_turma(jose_secretario.ler_turma("Turma2"))
    
    tela_login=TelaLogin(escola)

    #tela_login.cadastrar_usuario(usuario=jose_secretario,senha = "SenhaForte")
    #tela_login.cadastrar_usuario(usuario=mario_secretario, senha="SenhaFraca")
    #tela_login.cadastrar_usuario(usuario= jorge_professor, senha= "teste")
    
    tela_login.show_tela_login()



main()