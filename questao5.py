import math

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def maior_lado(self):
        return max(self.a, self.b, self.c)

    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

t = Triangulo(a, b, c)
print("Perímetro:", t.perimetro())
print("Maior lado:", t.maior_lado())
print("Área:", t.area())
