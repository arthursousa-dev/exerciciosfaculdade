# Divide o valor da conta entre as pessoas.
# Se o número de pessoas for 0 ou inválido, mostramos um erro.

try:
    total = float(input("Digite o valor total da conta: "))
    pessoas = int(input("Quantas pessoas vão dividir? "))
    if pessoas <= 0:
        raise ZeroDivisionError
    valor_por_pessoa = total / pessoas
    print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")
except (ValueError, ZeroDivisionError):
    print("Número de pessoas inválido para divisão da conta.")
