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


    def atribuir_nota_aluno(self, aluno, materia_nome, nome_atividade, nota):
        # Encontra a matéria
        materia = self.materia_dao.buscar_materia(materia_nome)
        if materia:
            # Verifica se a matéria já possui uma seção para o aluno
            if materia_nome not in aluno.notas:
                aluno.notas[materia_nome] = {'provas': {}, 'trabalhos': {}}
                
            # Atribui a nota conforme o tipo de atividade
            if nome_atividade in materia.provas:
                aluno.notas[materia_nome]['provas'][nome_atividade] = nota
            elif nome_atividade in materia.trabalhos:
                aluno.notas[materia_nome]['trabalhos'][nome_atividade] = nota
            
            # Salva as alterações
            self.aluno_dao.salvar_dados()
            self.materia_dao.salvar_dados()
        else:
            print(f"Matéria {materia_nome} não encontrada.")

    def atribuir_atividade_para_todos_alunos(self, materia_nome, tipo_atividade, nome_atividade, valor):
        self.materia_dao.adicionar_avaliacao(materia_nome, tipo_atividade, nome_atividade, valor)
   