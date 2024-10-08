

control = True
numero = None

while control:
    try:
        if numero is None:
            numero = int(input('Ingrese un número: '))
        control = False
    except ValueError as e:
        print('Ingrese un valor válido.')
        print(e)

print(f'Tabla de multiplicar del {numero}:')

for i in range(1, 11):
    resultado = numero * i
    print( str(numero) + ' x ' + str(i) + ' = ' + str(resultado) )