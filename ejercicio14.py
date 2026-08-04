# Modelar un pedido de restaurante.
# Crear una clase Cliente (nombre), una clase Item (nombre y precio privados)
# y una subclase ItemConDescuento que aplique un porcentaje de descuento al precio. 
# Crear una clase Pedido que contenga un Cliente y una lista de items, con un método total()
# y __str__ que muestre el cliente y el total a pagar.
# Comportamiento esperado:
# p = Pedido(Cliente("Sofía"))
# p.agregar(Item("Pizza", 400))
# p.agregar(ItemConDescuento("Postre", 200, 50))  # 50% off
# print(p.total())   # 500

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


class Item:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio


class ItemConDescuento(Item):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.__descuento = descuento

    def obtener_precio(self):
        precio_original = super().obtener_precio()
        return precio_original * (100 - self.__descuento) / 100


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def total(self):
        total = 0

        for item in self.items:
            total += item.obtener_precio()

        return total

    def __str__(self):
        return f"Cliente: {self.cliente.nombre} - Total: ${self.total()}"



p = Pedido(Cliente("Sofía"))
p.agregar(Item("Pizza", 400))
p.agregar(ItemConDescuento("Postre", 200, 50))  # 50% off
print(p.total())   # 500
