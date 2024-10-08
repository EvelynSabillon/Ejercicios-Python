import random


def generar_contrasenia(longitud):

    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()_+-=[]{}|;:,.<>?/'

    caracteres = mayusculas + minusculas + numeros + simbolos

    contrasenia = ""

    for i in range(longitud):
        contrasenia = contrasenia + random.choice(caracteres)

    return contrasenia


control = True
long = None

while control:
    try:
        if long is None:
            long = int(input('Ingrese la longitud de la contraseña (minimo 8): '))
        if long < 8:
            print('La longitud de la contraseña debe ser mayor o igual a 8.')
            long = None
        else:
            control = False
    except ValueError as e:
        print('Ingrese un valor válido, intente de nuevo.')
        print(e)
        long = None

contrasenia_generada = generar_contrasenia(long)

if contrasenia_generada:
    print('Contraseña generada: '+ contrasenia_generada)

