#criar um arquivo chamado "ola.txt" e escrever a palavra "Olá!" dentro dele.

try:
    with open("ola.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Olá!")  # Escreve a string no arquivo
    print("Arquivo 'ola.txt' criado com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao criar o arquivo: {e}")
