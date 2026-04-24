# Pede  idade e valida se o que foi digitado é um número inteiro.

try:
    idade = int(input("Digite sua idade: "))
    print("Idade registrada:", idade)
except ValueError:
    print("Por favor, insira uma idade válida (número inteiro).")
