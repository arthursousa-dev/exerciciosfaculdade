# Cadastra o nome e o preço de um produto, garantindo que o preço seja numérico.

try:
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    print(f"Produto '{nome}' cadastrado com sucesso! Preço: R$ {preco:.2f}")
except ValueError:
    print("Preço inválido. Digite apenas números para o valor do produto.")
