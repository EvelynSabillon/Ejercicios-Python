
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numero = int(input(f'Introduzca un número entero: '))

if es_primo(numero):
    print(f'El número '+str(numero)+' es primo.')
else:
    print(f'El número '+str(numero)+' no es primo.')