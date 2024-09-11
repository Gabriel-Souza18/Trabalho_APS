import unittest

from persistencia import *


class TestBaseDAOSingleton(unittest.TestCase):
    def test_singleton_aluno(self):
        instance1 = AlunoDAO()
        instance2 = AlunoDAO()
        instance3 = AlunoDAO()

        # Verificando se todas as instâncias são a mesma
        self.assertIs(instance1, instance2)
        self.assertIs(instance2, instance3)
        self.assertIs(instance1, instance3)

    def test_singleton_Professor(self):
        instance1 = ProfessorDAO()
        instance2 = ProfessorDAO()
        instance3 = ProfessorDAO()

        # Verificando se todas as instâncias são a mesma
        self.assertIs(instance1, instance2)
        self.assertIs(instance2, instance3)
        self.assertIs(instance1, instance3)

    def test_singleton_Secretario(self):
        instance1 = SecretarioDAO()
        instance2 = SecretarioDAO()
        instance3 = SecretarioDAO()

        # Verificando se todas as instâncias são a mesma
        self.assertIs(instance1, instance2)
        self.assertIs(instance2, instance3)
        self.assertIs(instance1, instance3)

    def test_singleton_Registro(self):
        instance1 = RegistroDAO()
        instance2 = RegistroDAO()
        instance3 = RegistroDAO()

        # Verificando se todas as instâncias são a mesma
        self.assertIs(instance1, instance2)
        self.assertIs(instance2, instance3)
        self.assertIs(instance1, instance3)


if __name__ == '__main__':
    unittest.main()
