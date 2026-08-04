# Crear una clase Mascota con nombre y un atributo privado energia que empiece en 100. El método jugar() baja la energía en 10 (sin bajar de 0) y dormir() la sube en 30 (sin pasar de 100). Exponer energia con property de solo lectura y agregar __str__.
# Comportamiento esperado:
# m = Mascota("Apolo")
# m.jugar()
# m.jugar()
# print(m)     	# Apolo - energía: 80
# m.dormir()
# print(m)     	# Apolo - energía: 100

class Mascota:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__energia=100
    
    def jugar(self):
        if(self.__energia <= 0):
            return "No tiene suficiente energia"
        self.__energia -=10
        if(self.__energia < 0):
            self.__energia=0
        
    def dormir(self):
        self.__energia +=30
        if(self.__energia > 100):
            self.__energia=100
    
    @property
    def energia(self):
        return self.__energia
    
    def __str__(self):
        return f"{self.__nombre} - energia:{self.__energia}"
    
    
m = Mascota("Apolo")
m.jugar()
m.jugar()
print(m)     	# Apolo - energía: 80
m.dormir()
print(m)     	# Apolo - energía: 100
