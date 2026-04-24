# Converte a temperatura digitada em Celsius para Fahrenheit.

try:
    celsius = float(input("Digite a temperatura em °C: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalem a {fahrenheit}°F.")
except ValueError:
    print("Erro: digite um valor numérico para a temperatura.")
