
numero = int(input('Ingrese un número: '))
print(f'Tabla de multiplicar del {numero}:')

for i in range(1, 11):
    resultado = numero * i
    print( str(numero) + ' x ' + str(i) + ' = ' + str(resultado) )