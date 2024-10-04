class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return print("No se puede dividir por 0")
        else:
            return a / b

calculadora1 = Calculadora()

continuar = "s"

while continuar == "s":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print("La suma de los números es: ", calculadora1.sumar(a, b))
    print("La resta de los números es: ", calculadora1.restar(a, b))
    print("La multiplicación de los números es: ", calculadora1.multiplicar(a, b))
    print("La división de los números es: ", calculadora1.dividir(a, b))

    continuar = input("¿Desea continuar? (s/n): ")

