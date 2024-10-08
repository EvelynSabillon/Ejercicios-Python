
class Libro:
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas):
        try:
            self.titulo = titulo
            self.autor = autor
            self.anio_publicacion = int(anio_publicacion)
            self.numero_paginas = int(numero_paginas)

            if self.anio_publicacion <= 0:
               print('El año de publicación debe ser un número positivo.')
            if self.numero_paginas <= 0:
                print('El número de páginas debe ser un número positivo.')

        except ValueError as e:
            print('Error: Los valores de año de publicación y número de páginas deben ser numéricos y positivos.')
            print(e)
            exit()

    def mostrar_informacion(self):
        print(f'Titulo: {self.titulo} \n'
              f'Autor: {self.autor} \n'
              f'Año de publicacion: {self.anio_publicacion} \n'
              f'Numero de paginas: {self.numero_paginas}')


libro1 = Libro('El principito', 'Antoine de Saint-Exupéry', 1943, 96)
libro1.mostrar_informacion()


print('---------')

libro2 = Libro('El señor de los anillos', 'J.R.R. Tolkien', 1954, 1178)
libro2.mostrar_informacion()