import unittest

import sys
sys.path.append('src')

from pessoas import *
from escola import *


class TestDiretor(unittest.TestCase):
    def setUp(self):
        self.diretor = Diretor("Carlos", 50, "12345")
        self.professor = Professor("Jose", 40,"212050", 1000)
        self.aluno = Aluno("Andre", 20, "67890","B3")
        self.turma = Turma("3B","Sala 101")

    def test_adicionar_turma(self):
        self.diretor.adicionar_turma(self.turma)
        self.assertIn(self.turma, self.diretor.turmas)

    def test_ler_escrever_turma(self):
        self.turma.adicionar_aluno(self.aluno)
        self.diretor.adicionar_turma(self.turma)
        self.diretor.escrever_turma("3B")
        self.diretor.ler_turma("3B", "Sala 102")
        turma_lida = self.diretor.turmas[-1]
        self.assertEqual(turma_lida.sala, "3B")
        self.assertEqual(turma_lida.alunos[0].nome, self.aluno.nome)

if __name__ == '__main__':
    unittest.main()
