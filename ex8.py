# pede 3 notas e calcula a média. Se o usuário digitar algo que não é número, mostramos um erro.

try:
    notas = [float(input(f"Nota {i+1}: ")) for i in range(3)]
    media = sum(notas) / 3
    print(f"Sua média é: {media:.2f}")
except ValueError:
    print("Digite apenas números para as notas.")
