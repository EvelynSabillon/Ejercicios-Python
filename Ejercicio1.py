class Rectangulo:
    def __init__(self, base, altura):
        try:
            self.base = float(base)
            self.altura = float(altura)
        except ValueError as e:  # El ValueError es un tipo de excepcion que se lanza cuando se intenta convertir un valor a un tipo numerico y no se puede
            print('Error: Los valores deben ser numericos')
            print(e)
            exit()

    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return (2 * self.base) + (2 * self.altura)


rectangulo1 = Rectangulo("s", 3)
print(f'El area del rectangulo es: {rectangulo1.area()}')
print(f'El perimetro del rectangulo es: {rectangulo1.perimetro()}')
