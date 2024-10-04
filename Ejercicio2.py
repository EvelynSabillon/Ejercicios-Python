
class Libro:
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print(f'Titulo: {self.titulo} \n'
              f'Autor: {self.autor} \n'
              f'Año de publicacion: {self.anio_publicacion} \n'
              f'Numero de paginas: {self.numero_paginas}')


libro1 = Libro('El principito', 'Antoine de Saint-Exupéry', 1943, 96)
libro1.mostrar_informacion()