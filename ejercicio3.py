# Crear una clase Termometro con un atributo privado temperatura, expuesto con property de lectura y escritura. 
# El setter debe lanzar ValueError si la temperatura es menor a -90 o mayor a 60.
# Comportamiento esperado:
# t = Termometro(20)
# t.temperatura = 35
# print(t.temperatura)   # 35
# t.temperatura = 200	# ValueError

class Termometro():
    def __init__(self, temperatura):
        self.__temperatura =  temperatura
        
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self,temperatura):
        if(temperatura < -90 or temperatura > 60):
            raise ValueError("error")
        self.__temperatura = temperatura
        
t = Termometro(20)
t.temperatura = 35
print(t.temperatura)   # 35
t.temperatura = 200	# ValueError

