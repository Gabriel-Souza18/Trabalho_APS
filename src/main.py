from pessoas import *
from escola import*


secretario =Secretario("Diretor",50,'3216516', "teste@gmail.com")

Turma1 = secretario.ler_turma("Turma1")
secretario.adicionar_turma(Turma1)

ze = Professor("ze", 40,'2165116', 10100, "ze@gmail.com")
carlos = Professor("carlos", 30,'252161',2000,"carlos@gmail.com")

matematica = Materia("matematica", ze)
portugues = Materia("portugues", carlos)
Turma1.adicionar_materia(matematica)
Turma1.adicionar_materia(portugues)

prova = Avaliacao(matematica, "24/05/2024")
ze.adicionar_prova(prova)

print(list(Turma1.materias))
matematica.imprimir_turmas()
#Turma1.imprimir_turma()