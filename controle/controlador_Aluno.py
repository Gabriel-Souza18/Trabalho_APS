class ControladorAluno:
    def __init__(self, aluno_dao, turma_dao, materia_dao):
        self.aluno_dao = aluno_dao
        self.turma_dao = turma_dao
        self.materia_dao = materia_dao

    def obter_materias(self, aluno):
        # Busca as matérias do aluno
        nomes_materias = list(aluno.notas.keys())
        lista_materias = [self.materia_dao.buscar_materia(nome) for nome in nomes_materias]
        return lista_materias

    def obter_alunos_turma(self, turma):
        # Busca os alunos de uma turma
        alunos = []

        for aluno in turma.alunos:
            alunos.append(aluno)
        
        return alunos

    def obter_notas_materia(self, aluno, materia):
        # Retorna as notas do aluno em uma matéria 
        return aluno.notas.get(materia.nome, {})
    
    def exibir_materia(self, materia, aluno):
        print(materia, "\n", aluno)


