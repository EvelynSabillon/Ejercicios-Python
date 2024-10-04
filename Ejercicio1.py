class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return (2 * self.base) + (2 * self.altura)

rectangulo1 = Rectangulo(5, 3)
print(f'El area del rectangulo es: {rectangulo1.area()}')
print(f'El perimetro del rectangulo es: {rectangulo1.perimetro()}')
