# Crear una clase Rectangulo con atributos privados base y altura, y properties de solo lectura area y perimetro calculadas a partir de ellos. 
# Agregar __str__.
# Comportamiento esperado:
# r = Rectangulo(4, 3)
# print(r.area)    	# 12
# print(r.perimetro)   # 14
# print(r)         	# Rectángulo 4x3 (área: 12)

class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
        self.__area = base * altura
        self.__perimetro = (base + altura) * 2
    
    @property
    def area(self):
        return self.__area
    
    @property
    def perimetro(self):
        return self.__perimetro
    
    def __str__(self):
        return f"Rectángulo {self.__base}x{self.__altura} (área: {self.__area})"
    
r = Rectangulo(4, 3)
print(r.area)    	# 12
print(r.perimetro)   # 14
print(r)         	# Rectángulo 4x3 (área: 12)
