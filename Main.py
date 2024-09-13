from controle.controlador_Login import Controlador_Login
from persistencia.TurmaDAO import TurmaDAO
from persistencia.AlunoDAO import AlunoDAO  # Supondo que exista um AlunoDAO
from persistencia.MateriaDAO import MateriaDAO  # Supondo que exista um MateriaDAO
from persistencia.ProfessorDAO import ProfessorDAO


def main():
    # Inicializa o controlador de login
    controlador_login = Controlador_Login()
    controlador_login.iniciar()


if __name__ == "__main__":
    main()
