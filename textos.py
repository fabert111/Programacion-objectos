class Texto:
    def __init__(self, contenido):
        self._contenido = contenido

    def libros(self):
        print(f"Este libro es de contenido ({self._contenido }), por lo tanto no es recomendado para todas las edades")

    def get_contenido(self):
        return self._contenido
    def set_contenido(self,contenido):
        self._contenido = contenido

librito = Texto("Novela Romántica +18")
librito.libros()

class Libro(Texto):
    def __init__(self, contenido, autor):
        super().__init__(contenido)
        self._autor = autor

    def libros(self):
        print(f"Este libro es de {self._autor} por la tanto su contenido ({self._contenido }), es recomendado para todas las edades")

    def get_autor(self):
        return self._autor
    
libro1 = Libro("cuentos infantiles +5", "Charles Perraul")
print("")
libro1.libros()