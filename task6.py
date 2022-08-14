class Vehiculo :

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo) :

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


c = Coche('rojo', 4, 4, 100, 4)
print(c)


#tarea 2

class Alumno :

    def __init__(self, nombre, nota = 0):
        self.nombre = nombre
        self.nota = nota

    def asignarNota(self, n) :
        self.nota = n

    def obtenerNota(self) :
        return self.nota

    def aprobado(self) :
        return "aprobado" if self.nota >= 3 else "no aprobado" 

    def nombreAlumno(self) :
        return self.nombre