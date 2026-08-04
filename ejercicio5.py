# Crear una clase Libro con los atributos titulo e isbn. Dos libros se consideran iguales si tienen el mismo ISBN: implementar __eq__. Agregar __str__.
# Comportamiento esperado:
# l1 = Libro("Python", "978-1")
# l2 = Libro("PYTHON 3", "978-1")
# l3 = Libro("Java", "978-2")
# print(l1 == l2)   # True
# print(l1 == l3)   # False

class Libro():
     
     def __init__(self, titulo, isbn):
         self.__titulo = titulo
         self.__isbn = isbn
         
     def __eq__(self, otro):
      
        return self.__isbn == otro.__isbn
    
     def __str__(self):
        return f"Libro:{self.__titulo}, isbn:{self.__isbn}"
    
l1 = Libro("Python", "978-1")
l2 = Libro("PYTHON 3", "978-1")
l3 = Libro("Java", "978-2")
print(l1 == l2)   # True
print(l1 == l3)   # False
