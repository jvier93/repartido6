# Crear una clase Empleado con nombre y salario y un método aumentar_salario(monto). Crear una clase Gerente que herede de Empleado y sobrescriba aumentar_salario para que además sume un bono fijo de $5000 cada vez. Definir __eq__ para comparar empleados por su salario.
# Comportamiento esperado:
# emp = Empleado("Juan", 30000)
# gte = Gerente("Ana", 30000)
# emp.aumentar_salario(2000)
# gte.aumentar_salario(2000)
# print(emp.salario)   # 32000
# print(gte.salario)   # 37000
# print(emp == gte)	# False

class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    def aumentar_salario(self, monto):
        self.__salario += monto

    def __eq__(self, otro):
        return self.__salario == otro.__salario
        
class Gerente(Empleado):
    
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        self.bono = 5000
    
    def aumentar_salario(self, monto):
        super().aumentar_salario(monto + self.bono)
        

emp = Empleado("Juan", 30000)
gte = Gerente("Ana", 30000)
emp.aumentar_salario(2000)
gte.aumentar_salario(2000)
print(emp.salario)   # 32000
print(gte.salario)   # 37000
print(emp == gte)	# False
