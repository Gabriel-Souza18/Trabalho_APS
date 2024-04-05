import unittest
from pessoas import Aluno, Professor, Diretor
from escola import Turma


class TestDiretor(unittest.TestCase):
    def setUp(self):
        self.diretor = Diretor("Carlos", 50, "12345")
        self.professor = Professor("Jose", 40,"212050", 1000)
        self.aluno = Aluno("Andre", 20, "67890",0,"B3")
        self.turma = Turma("Sala 101")

    def test_adicionar_turma(self):
        self.diretor.adicionar_turma(self.turma)
        self.assertIn(self.turma, self.diretor.turmas)

    def test_ler_escrever_turma(self):
        self.turma.adicionar_aluno(self.aluno)
        self.diretor.adicionar_turma(self.turma)
        self.diretor.escrever_turma("Sala 101")
        self.diretor.ler_turma("Sala 101", "Sala 102")
        turma_lida = self.diretor.turmas[-1]
        self.assertEqual(turma_lida.sala, "Sala 102")
        self.assertEqual(turma_lida.alunos[0].nome, self.aluno.nome)

if __name__ == '__main__':
    unittest.main()
