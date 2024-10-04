import random


def generar_contrasenia(longitud):
    if longitud < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return None

    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()_+-=[]{}|;:,.<>?/'

    caracteres = mayusculas + minusculas + numeros + simbolos

    contrasenia = ""

    for i in range(longitud):
        contrasenia = contrasenia + random.choice(caracteres)

    return contrasenia


long = int(input('Ingrese la longitud de la contraseña (minimo 8): '))

contrasenia_generada = generar_contrasenia(long)

if contrasenia_generada:
    print('Contraseña generada: '+ contrasenia_generada)

