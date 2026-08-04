# Crear una clase CuentaBancaria con un atributo privado saldo que empiece en 0 y un método depositar(monto). El saldo debe leerse mediante una property de solo lectura (no se puede modificar directamente desde afuera).
# Comportamiento esperado:
# c = CuentaBancaria()
# c.depositar(500)
# c.depositar(300)
# print(c.saldo)   # 800

class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0
   
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    @property
    def saldo(self):
        return self.__saldo

c = CuentaBancaria()
c.depositar(500)
c.depositar(300)
print(c.saldo)   # 800