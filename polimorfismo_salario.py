class Empleado:
    def __init__(self, nombre, sueldomMensual, sueldoMensualPalabras):
        self.nombre = nombre
        self.sueldoMensual = sueldomMensual
        self.sueldoMensualPalabras = sueldoMensualPalabras

    def sueldoanual(self):
        salario = 12*self.sueldoMensual*(1 + 1/100)
        print(f"Mensualmente {self.nombre} se gana {self.sueldoMensualPalabras} ({self.sueldoMensual})💸 como empleado")

class Policia(Empleado):
    def __init__(self, nombre, sueldomMensual, sueldoMensualPalabras):
        super().__init__(nombre, sueldomMensual, sueldoMensualPalabras)

    def sueldoanual(self):
        salario = 12*self.sueldoMensual*(1 + 18/100)
        print(f"Mensualmente {self.nombre} se gana {self.sueldoMensualPalabras} ({self.sueldoMensual})💸 como policia")

class Mesero(Empleado):
    def __init__(self, nombre, sueldomMensual, sueldoMensualPalabras):
        super().__init__(nombre, sueldomMensual, sueldoMensualPalabras)

    def sueldoanual(self):
        salario = 12*self.sueldoMensual*(1 + 8/100)
        print(f"Mensualmente {self.nombre} se gana {self.sueldoMensualPalabras} ({self.sueldoMensual})💸 como mesero")

empleados = [
    Empleado("Enrique", 1160000, "un millón ciento sesenta mil"),
    Policia("Camilo", 1760000, "un millón setecientos sesenta mil"),
    Mesero("Luis", 1360000, "un millón trescientos sesenta mil")
]

for empleado in empleados:
    empleado.sueldoanual()
