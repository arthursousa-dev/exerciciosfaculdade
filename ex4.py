# criar um arquivo com os números de 1 a 100 separados por ponto e vírgula (;).

try:
    with open("crescente.txt", "w", encoding="utf-8") as arquivo:
        numeros = ";".join(str(i) for i in range(1, 101))
        arquivo.write(numeros)
    print("Arquivo 'crescente.txt' criado com sucesso!")
except Exception as e:
    print(f"Erro ao criar o arquivo: {e}")
