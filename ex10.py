#  Usuário escolhe um dia do mês para agendar. Valida se está entre 1 e 31.

try:
    dia = int(input("Digite o dia do mês (1 a 31): "))
    if not (1 <= dia <= 31):
        raise ValueError
    print(f"Sua consulta foi agendada para o dia {dia}.")
except ValueError:
    print("Dia inválido! Digite um número entre 1 e 31.")
