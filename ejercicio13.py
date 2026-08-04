# Crear una clase Jugador con nombre y numero privados, donde dos jugadores son iguales si tienen el mismo número (__eq__).
# Crear una clase Arquero que herede de Jugador y agregue atajadas y el método atajar().
# Crear una clase Equipo con una lista de jugadores, cuyo método agregar(jugador) no permita dos jugadores con el mismo número.
# Comportamiento esperado:
# e = Equipo("Nacional")
# e.agregar(Jugador("Pérez", 10))
# e.agregar(Arquero("Muslera", 1))
# e.agregar(Jugador("Otro", 10))   # rechazado: número repetido
# print(len(e.jugadores))      	# 2


class Jugador:
    def __init__(self, nombre, numero):
        self.__nombre = nombre
        self.__numero = numero

    def obtener_nombre(self):
        return self.__nombre

    def obtener_numero(self):
        return self.__numero

    def __eq__(self, otro):
        return self.__numero == otro.__numero
        


class Arquero(Jugador):
    def __init__(self, nombre, numero):
        super().__init__(nombre, numero)
        self.__atajadas = 0

    def atajar(self):
        self.__atajadas += 1

    def obtener_atajadas(self):
        return self.__atajadas


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar(self, jugador):
        if jugador in self.jugadores:
            print("Jugador rechazado: número repetido")
            return

        self.jugadores.append(jugador)




e = Equipo("Nacional")

e.agregar(Jugador("Pérez", 10))
e.agregar(Arquero("Muslera", 1))
e.agregar(Jugador("Otro", 10))  # rechazado

print(len(e.jugadores))  # 2