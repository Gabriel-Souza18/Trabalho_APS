from controle.ControladorLogin import ControladorLogin
from persistencia.TurmaDAO import TurmaDAO
from persistencia.AlunoDAO import AlunoDAO  # Supondo que exista um AlunoDAO
from persistencia.MateriaDAO import MateriaDAO  # Supondo que exista um MateriaDAO
from persistencia.ProfessorDAO import ProfessorDAO


def main():
    # Inicializa o controlador de login
    controlador_login = ControladorLogin()
    controlador_login.iniciar_tela_login()


if __name__ == "__main__":
    main()
