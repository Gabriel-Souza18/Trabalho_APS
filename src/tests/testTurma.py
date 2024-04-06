import unittest
import sys
sys.path.append('src')

from pessoas import*
from escola import *


class TestTurma(unittest.TestCase):
    def setUp(self):
        self.turma = Turma("Sala 101")
        self.aluno = Aluno("João", 12,"123",10,'b3')
        self.professor = Professor("Maria",40,"321321",1000)
        self.materia = Materia("Matemática", self.professor)

    def test_adicionar_aluno(self):
        self.turma.adicionar_aluno(self.aluno)
        self.assertIn(self.aluno, self.turma.alunos)


    def test_adicionar_materia(self):
        self.turma.adicionar_materia(self.materia)
        self.assertIn(self.materia, self.turma.materias)

if __name__ == '__main__':
    unittest.main()
