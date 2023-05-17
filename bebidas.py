class Bebida:
    def __init__(self, nombre, empresa):
        self._nombre = nombre
        self.empresa = empresa

    def marca_nombre (self):
        print(f"Es una {self._nombre} y hace parte de {self.empresa} ")

    def get_nombre(self):
        return self._nombre
    def set_nombre(self,nombre):
        self._nombre = nombre

bebida = Bebida("Fanta", "CocaCola")
bebida.marca_nombre()

bebida.set_nombre("Sprite")
print(bebida.get_nombre())
print("")
class Saludable(Bebida):
    def __init__(self, nombre, empresa, origen):
        super().__init__(nombre, empresa)
        self._origen = origen

    def marca_nombre (self):
        print(f"Es una bebida natural llamada {self._nombre} y es derivada del {self.empresa} y su origen es {self._origen} ")

    def get_origen(self):
        return self._origen
    def set_origen(self,origen):
        self._origen = origen   

natural = Saludable("zumo de naranja", "campo", "natural")
natural.marca_nombre()

natural.set_origen("jugo de Guayaba")
print(natural.get_origen())
print("")