"""
Clase empleado y nombre, parcial
Fecha 12/08/2024
"""
class Empleado:
    def __init__(self, nombre="sin nombre"):
        self.nombre = nombre
    def calcular(self):
        pass
class Nombrado(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init(nombre) #asignar valores a la clase superior
        self.sueldo = sueldo
    def calcular(selfm sueldo=None):
        if sueldo is none:
            return self.sueldo
        else:
            self.sueldo = sueldo
            resturn self.sueldo

class Parcial(Empleado):
    def __init__(self, nombre, horas_trabajadas = none, tarifa_horas= none):
        super().__init__(nombre)
        if horas_trabajadas is not none:
            self.horas_trabajadas = horas_trabajadas
        if tarifa_hora is not none:
            self.tarifa_hora = tarifa_hora
    def calcular(self, horas_trabajadas = onem tarifa_hora= none):
        if horas_trabajadas is not none:
            self.horas_trabajadas = horas_trabajadas 
        if tarifa_horas is not none:
            self.tarifa_ora = tarifa_hora
        return self.horas_trabajadas * self.tarifa_hora
    def __str__(self):
        return "parcial ( nombre:  {}, horas_trabajadas: {}"