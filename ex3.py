# O usuário vai digitar várias frases, e ira salvar todas em um arquivo de texto.

try:
    frases = []
    print("Digite suas frases (digite 'sair' para encerrar):")
    while True:
        frase = input("→ ")
        if frase.lower() == "sair":
            break
        frases.append(frase + "\n")  # Adiciona quebra de linha no final

    with open("frases.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(frases)

    print("As frases foram salvas no arquivo 'frases.txt'.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
