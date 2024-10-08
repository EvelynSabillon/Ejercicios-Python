import random

numero_aleatorio = random.randint(1, 100)
contador = 0

print('¡Adivina el número entre 1 y 100!')



while True:
    control = True
    numero = None

    while control:
        try:
            if numero is None:
                numero = int(input('Ingresa tu intento: '))
            control = False
        except ValueError as e:
            print('Ingrese un valor válido, intente de nuevo.')
            print(e)

    contador += 1
    if numero < numero_aleatorio:
        print('El número es mayor.')
    elif numero > numero_aleatorio:
        print('El número es menor.')
    else:
        print('¡Felicitaciones! Has adivinado el número en ' + str(contador) + ' intentos.')
        break


