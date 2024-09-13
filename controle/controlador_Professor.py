class ControladorProfessor:
    def __init__(self, professor_dao, aluno_dao, turma_dao, materia_dao):
        self.professor_dao = professor_dao
        self.turma_dao = turma_dao
        self.materia_dao = materia_dao
        self.aluno_dao = aluno_dao

    def obter_materias(self, professor):
        # Busca as matérias do professor
        materias = self.materia_dao.buscar_materias_por_professor(professor.registro)
        return materias

    def obter_turmas_professor(self, professor):
        # Busca as turmas associadas a um professor
        turmas = []
        materias = self.materia_dao.buscar_materias_por_professor(professor.registro)
        for materia in materias:
            turma = self.turma_dao.buscar_turma(materia.turma.nome_turma)
            if turma and turma not in turmas:
                turmas.append(turma)
        return turmas

    def obter_notas_materia(self, professor, materia):
        # Retorna as notas do professor em uma matéria
        return materia.notas.get(professor.nome, {})

    def obter_alunos_por_turma(self, turma):
        # Retorna uma lista de alunos para a turma fornecida
        alunos = [aluno for aluno in self.aluno_dao.buscar_alunos() if aluno.turma == turma.nome_turma]
        return alunos

    def obter_materias_do_aluno(self, aluno):
        # Retorna uma lista de matérias associadas ao aluno
        nomes_materias = list(aluno.notas.keys())
        lista_materias = [self.materia_dao.buscar_materia(nome) for nome in nomes_materias]
        return lista_materias


    def atribuir_nota(self, aluno, materia_nome, nota):
        # Atribui uma nota ao aluno para uma matéria específica
        materia = self.materia_dao.buscar_materia(materia_nome)
        if materia:
            if aluno.matricula not in materia.notas:
                materia.notas[aluno.matricula] = {}
            materia.notas[aluno.matricula][materia_nome] = nota
            self.materia_dao.salvar_materias()  # Salvar alterações no JSON
        else:
            print(f"Matéria {materia_nome} não encontrada.")
