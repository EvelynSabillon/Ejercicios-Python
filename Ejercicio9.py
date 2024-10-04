import random

numero_aleatorio = random.randint(1, 100)
contador = 0

print('¡Adivina el número entre 1 y 100!')

while True:
    numero = int(input('Ingresa tu intento: '))
    contador += 1
    if numero < numero_aleatorio:
        print('El número es mayor.')
    elif numero > numero_aleatorio:
        print('El número es menor.')
    else:
        print('¡Felicitaciones! Has adivinado el número en ' + str(contador) + ' intentos.')
        break


