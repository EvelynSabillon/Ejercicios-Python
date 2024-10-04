
def contar_vocales(frase):
    vocales = ['a', 'e', 'i', 'o', 'u']
    total_vocales = 0
    for vocal in frase:
        if vocal in vocales:
            total_vocales += 1
    return total_vocales

frase = input('Introduzca una frase: ')
print(f'La frase tiene un total de: ' + str(contar_vocales(frase)) + ' vocales.')