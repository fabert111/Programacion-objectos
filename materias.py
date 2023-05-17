class Materia:
    def __init__(self, nombre):
        self._nombre = nombre

    def coleguio(self):
        print(f"mi materia favorita es {self._nombre}")

    def get_nombre(self):
        return self._nombre
    def set_nombre(self,nombre):
        self._nombre = nombre

materias = Materia("Edu.fisica")
materias.coleguio()

materias.set_nombre("o tambien informatica")
print(materias.get_nombre())
print("")

class Asignatura(Materia):
    def __init__(self, nombre, profesor):
        super().__init__(nombre)
        self._profesor = profesor
    
    def coleguio(self):
        print(f"mi materia favorita es {self._nombre} ademas de que la profesora {self._profesor} es muy amable")

    def get_profesor(self):
        return self._profesor
    def set_profesor(self,profesor):
        self._profesor = profesor
    
alumno = Asignatura("Matematicas", "Maria")
alumno.coleguio()

alumno.set_profesor("tambien dicta español")
print(alumno.get_profesor())
print("")

