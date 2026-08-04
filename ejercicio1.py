
# Crear una clase Persona con los atributos nombre y edad. 
# Definir __init__ para inicializarla y __str__ para mostrar sus datos.
# Comportamiento esperado:

# p = Persona("Lucía", 25)
# print(p)    	# Lucía, 25 años


class Persona:
 def __init__(self,nombre, edad):
     self.nombre = nombre
     self.edad = edad

 def __str__(self):
    return f"{self.nombre}, {self.edad}"

p = Persona("Lucía", 25)
print(p)    	# Lucía, 25 años
