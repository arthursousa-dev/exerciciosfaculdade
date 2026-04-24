# O usuário digita o nome de um arquivo .txt , tentamos abrir-lo.
# Se o arquivo não existir, mostramos uma mensagem .

try:
    nome_arquivo = input("Digite o nome do arquivo (.txt): ")
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
