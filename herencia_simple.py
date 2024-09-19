class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre =nombre
        self.edad =edad
        self.salario = salario

    def calcular_bono(self):
        return self.salario * 0.1

class gerente (Empleado):
    def _init_(self, nombre, edad, salario, departamento):
        super(). _init_(nombre, edad, salario)
        self.departamento = departamento

    def calcular_bono(self):
        return self.salario * 0.2
