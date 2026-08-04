# Crear una clase Cuenta con saldo privado y métodos depositar y extraer, donde extraer no permite dejar el saldo negativo. Crear CajaDeAhorro (igual que la base) y CuentaCorriente, que sobrescriba extraer para permitir quedar en negativo hasta un límite de descubierto.
# Comportamiento esperado:
# cc = CuentaCorriente(1000, descubierto=10000)
# cc.extraer(5000)
# print(cc.saldo)   # -4000
# cc.extraer(50000) # no permitido


class Cuenta():
    def __init__(self,saldo):
        self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
        
    def depositar(self, monto):
        self.__saldo = self.__saldo + monto
        
    
    def extraer(self, monto):
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo = self.__saldo - monto 
        
class CajaDeAhorro(Cuenta):
    pass


class CuentaCorriente(Cuenta):
    def __init__(self, saldo, descubierto):
        super().__init__(saldo)
        self.__descubierto = descubierto
        
    def extraer(self, monto):
        if monto > (self.saldo + self.__descubierto):
            raise ValueError("Saldo insuficiente")
        self.saldo = self.saldo - monto   
        
    

cc = CuentaCorriente(1000, descubierto=10000)
cc.extraer(5000)
print(cc.saldo)   # -4000
cc.extraer(50000) # no permitido
