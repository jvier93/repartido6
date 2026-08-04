import math
# Crear una clase Figura con un método area() (que devuelva 0) y dos clases hijas Circulo (con radio) y Cuadrado (con lado), cada una con su propio cálculo de area() y su __str__.
# Comportamiento esperado:
# c = Circulo(2)
# q = Cuadrado(3)
# print(round(c.area(), 2))   # 12.57
# print(q.area())         	# 9

class Figura:
    def area(self):
        return 0

class Circulo(Figura):
    
    def __init__(self,radio):
        self.__radio = radio
        
    def area(self):
        return math.pi * (self.__radio **2) 
        
    
class Cuadrado(Figura):
    
    def __init__(self,lado):
        self.__lado = lado
        
    def area(self):
        return self.__lado**2

c = Circulo(2)
q = Cuadrado(3)
print(round(c.area(), 2))   # 12.57
print(q.area())         	# 9