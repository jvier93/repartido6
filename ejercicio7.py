# Crear una clase Vehiculo con atributos marca y velocidad_maxima, y dos clases hijas Auto y Moto que hereden de ella usando super(). Cada hija debe tener su propio __str__ indicando el tipo de vehículo.
# Comportamiento esperado:
# a = Auto("Toyota", 180)
# mo = Moto("Honda", 200)
# print(a)	# Auto Toyota (máx: 180 km/h)
# print(mo)   # Moto Honda (máx: 200 km/h)

class Vehiculo():
    def __init__(self, marca, velocidad_maxima):
        self.__marca = marca
        self.__velocidad_maxima = velocidad_maxima
        
    @property
    def marca(self):
        return self.__marca
    
    @property
    def velocidad_maxima(self):
        return self.__velocidad_maxima
        
class Auto(Vehiculo):
    def __init__(self, marca,velocidad_maxima):
        super().__init__( marca,velocidad_maxima)
        
    def __str__(self):
        return f"Auto {super().marca} (máx: {super().velocidad_maxima} km/h)"
    

class Moto(Vehiculo):
     def __init__(self, marca,velocidad_maxima):
            super().__init__( marca,velocidad_maxima)

     def __str__(self):
         return f"Moto {super().marca} (máx: {super().velocidad_maxima} km/h)"


a = Auto("Toyota", 180)
mo = Moto("Honda", 200)
print(a)	# Auto Toyota (máx: 180 km/h)
print(mo)   # Moto Honda (máx: 200 km/h)