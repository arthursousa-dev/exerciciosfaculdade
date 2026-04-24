class Carro:
    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa

    def descricao(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - {self.cor} - Placa: {self.placa}"

carros = [
    Carro("Fiat", "Uno", 2010, "Prata", "ABC1A10"),
    Carro("Volkswagen", "Gol", 2015, "Preto", "DEF2B20"),
    Carro("Chevrolet", "Onix", 2019, "Branco", "GHI3C30"),
    Carro("Toyota", "Corolla", 2020, "Azul", "JKL4D40"),
    Carro("Honda", "Civic", 2018, "Cinza", "MNO5E50"),
    Carro("Renault", "Kwid", 2021, "Vermelho", "PQR6F60"),
    Carro("Hyundai", "HB20", 2017, "Prata", "STU7G70"),
    Carro("Ford", "Ka", 2016, "Preto", "VWX8H80"),
    Carro("Nissan", "March", 2014, "Branco", "YZA9I90"),
    Carro("Jeep", "Renegade", 2022, "Verde", "BCD0J00"),
]

for c in carros:
    print(c.descricao())
