#  Crear una clase Motor con atributos cilindrada y encendido (empieza apagado) y métodos encender() y apagar(). Crear una clase Auto que contenga un objeto Motor (composición) y métodos arrancar() y detener() que actúen sobre su motor. Agregar __str__ que informe si el motor está encendido.
# Comportamiento esperado:
# a = Auto("Fiat", 1400)
# a.arrancar()
# print(a)   # Auto Fiat - motor encendido
# a.detener()
# print(a)   # Auto Fiat - motor apagado


class Motor:
    def __init__(self, cilindrada):
        self.__cilindrada = cilindrada
        self.__encendido = False
        
    def encender(self):
        self.__encendido = True
        
    def apagar(self):
        if self.__encendido:
            self.__encendido = False
        
    @property
    def encendido(self):
        return self.__encendido
    

class Auto:
    def __init__(self, marca, cilindrada):
        self.__marca = marca
        self.__motor = Motor(cilindrada)
        
    def arrancar(self):
        self.__motor.encender()
        
    def detener(self):
        self.__motor.apagar()
        
    def __str__(self):
        estado_motor = "encendido" if self.__motor.encendido else "apagado"
        return f"Auto {self.__marca} - motor {estado_motor}"
    
a = Auto("Fiat", 1400)
a.arrancar()
print(a)   # Auto Fiat - motor encendido
a.detener()
print(a)   # Auto Fiat - motor apagado
