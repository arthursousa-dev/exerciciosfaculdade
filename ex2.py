#  abrir o arquivo que criado  anteriormente e ler o que está dentro.

try:
    with open("ola.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()  # Lê todo o conteúdo
        print("Conteúdo do arquivo:", conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado. Talvez ele ainda não exista?")
except Exception as e:
    print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")
