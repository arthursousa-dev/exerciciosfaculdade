# irá salvar os números de 100 até 1, um em cada linha.
 
try:
    with open("decrescente.txt", "w", encoding="utf-8") as arquivo:
        for i in range(100, 0, -1):
            arquivo.write(f"{i}\n")
    print("Arquivo 'decrescente.txt' criado com sucesso!")
except Exception as e:
    print(f"Erro ao criar o arquivo: {e}")
