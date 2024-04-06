from pessoas import *
from escola import*


diretor =Diretor("Diretor",50,'3216516')
Turma1 = diretor.ler_turma("Turma1",1.1)
diretor.adicionar_turma(Turma1)

ze = Professor("ze", 40,'2165116', 10100)

matematica = Materia("matematica", ze)
ze.adicionar_materia(matematica)
Turma1.adicionar_materia(matematica)
Turma1.imprimir_turma()