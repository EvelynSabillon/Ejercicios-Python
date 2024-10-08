
def fibonacci(n):
    a = 0
    b = 1
    lista = []

    for i in range(n):
        lista.append(a)
        temp = a
        a = b
        b = temp + b

    secuencia = ""

    for i in range(len(lista)):
        secuencia += str(lista[i])
        if i < len(lista) - 1:
            secuencia += ', '
    print(secuencia)

control = True
numero = None

while control:
    try:
        if numero is None:
            numero = int(input('Ingrese el número de términos: '))
        control = False
    except ValueError as e:
        print('Ingrese un valor válido.')
        print(e)

print('Secuencia de Fibonacci: ')
fibonacci(numero)