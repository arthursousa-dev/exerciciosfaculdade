class Aluno:
    def __init__(self, nome, curso, tempoSemDormir=0):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self, horas):
        self.tempoSemDormir += horas

    def dormir(self, horas):
        self.tempoSemDormir = max(0, self.tempoSemDormir - horas)

a = Aluno("Mariana", "ADS", 5)
a.estudar(10)
print("Tempo sem dormir após estudar:", a.tempoSemDormir)
a.dormir(8)
print("Tempo sem dormir após dormir:", a.tempoSemDormir)
