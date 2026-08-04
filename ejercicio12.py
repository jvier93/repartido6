#  Reutilizando la clase Producto (nombre y precio privados, con property), crear una clase Carrito que contenga una lista de productos con los métodos agregar(producto), total() (suma de los precios) y __str__ que liste los productos y muestre el total.
# Comportamiento esperado:
# c = Carrito()
# c.agregar(Producto("Pan", 50))
# c.agregar(Producto("Leche", 80))
# print(c.total())   # 130

class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
class Carrito:
    def __init__(self):
        self.__productos = []
        
    def agregar(self, producto):
        self.__productos.append(producto)
        
    def total(self):
        return sum(producto.precio for producto in self.__productos)
    
    def __str__(self):
     texto = f"Total: ${self.total()} "
     for producto in self.__productos:
        texto += f"{producto.nombre} - ${producto.precio}"
    
     return texto

c = Carrito()
c.agregar(Producto("Pan", 50))
c.agregar(Producto("Leche", 80))
print(c.total())   # 130
