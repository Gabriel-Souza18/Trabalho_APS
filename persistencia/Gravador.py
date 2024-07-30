import json
import random
from controle import Escola
from persistencia import Leitor

class Gravador:
    def __init__(self, escola: Escola):
        self.escola = escola

    def _gerar_senha(self):
        return ''.join(random.choices('0123456789', k=3))

    def _carregar_registros(self):
        try:
            with open(Leitor.CAMINHO + 'registro.json', 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return []

    def _salvar_registros(self, registros):
        registros_atuais = set(
            list(self.escola.Professores.keys()) +
            list(self.escola.Alunos.keys()) +
            list(self.escola.Secretarios.keys())
        )
        registros = [reg for reg in registros if reg["registro"] in registros_atuais]

        with open(Leitor.CAMINHO + 'registro.json', 'w', encoding='utf-8') as arquivo:
            json.dump(registros, arquivo, indent=4, ensure_ascii=False)

    def _registro_existe(self, registro, registros):
        return any(reg['registro'] == registro for reg in registros)

    def gravar_professores(self):
        professores = [
            {
                "nome": professor.nome,
                "idade": professor.idade,
                "email": professor.email,
                "registro": professor.registro,
                "salario": professor.salario
            }
            for professor in self.escola.Professores.values()
        ]
        with open(Leitor.CAMINHO + "professores.json", "w", encoding="utf-8") as arquivo:
            json.dump(professores, arquivo, indent=4, ensure_ascii=False)

        registros = self._carregar_registros()
        for professor in self.escola.Professores.values():
            if not self._registro_existe(professor.registro, registros):
                senha = self._gerar_senha()
                registros.append({
                    "registro": professor.registro,
                    "senha": senha,
                    "tipo": 'P'
                })
        self._salvar_registros(registros)

    def gravar_alunos(self):
        alunos = [
            {
                "nome": aluno.nome,
                "idade": aluno.idade,
                "email": aluno.email,
                "matricula": aluno.matricula,
                "turma": aluno.turma,
                "notas": aluno.notas
            }
            for aluno in self.escola.Alunos.values()
        ]
        with open(Leitor.CAMINHO + "alunos.json", "w", encoding="utf-8") as arquivo:
            json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

        registros = self._carregar_registros()
        for aluno in self.escola.Alunos.values():
            if not self._registro_existe(aluno.matricula, registros):
                senha = self._gerar_senha()
                registros.append({
                    "registro": aluno.matricula,
                    "senha": senha,
                    "tipo": 'A'
                })
        self._salvar_registros(registros)

    def gravar_secretarios(self):
        secretarios = [
            {
                "nome": secretario.nome,
                "idade": secretario.idade,
                "email": secretario.email,
                "registro": secretario.registro,
                "salario": secretario.salario
            }
            for secretario in self.escola.Secretarios.values()
        ]
        with open(Leitor.CAMINHO + "secretarios.json", "w", encoding="utf-8") as arquivo:
            json.dump(secretarios, arquivo, indent=4, ensure_ascii=False)

        registros = self._carregar_registros()
        for secretario in self.escola.Secretarios.values():
            if not self._registro_existe(secretario.registro, registros):
                senha = self._gerar_senha()
                registros.append({
                    "registro": secretario.registro,
                    "senha": senha,
                    "tipo": 'S'
                })
        self._salvar_registros(registros)

    def gravar_materias(self):
        materias = [
            {
                "nome": materia.nome,
                "professor": materia.professor.nome,
                "turma": materia.turma,
                "provas": materia.provas,
                "trabalhos": materia.trabalhos
            }
            for materia in self.escola.Materias.values()
        ]
        with open(Leitor.CAMINHO + "materias.json", "w", encoding="utf-8") as arquivo:
            json.dump(materias, arquivo, indent=4, ensure_ascii=False)

    def gravar_registros(self, registro, senha, tipo):
        registros = self._carregar_registros()
        registros.append({
            "registro": registro,
            "senha": senha,
            "tipo": tipo
        })
        self._salvar_registros(registros)
