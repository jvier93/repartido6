# Crear una clase Material con título y código. 
# De Material heredan Libro (con autor) y Revista (con número de edición),
# cada una con su __str__.
# Crear una clase Socio con nombre y una lista privada de materiales prestados,
# y una clase Biblioteca que contenga materiales y socios, con los métodos:
# a.  prestar(codigo, socio): si el material existe y está disponible,
# se lo asigna al socio y deja de estar disponible.
# b.  devolver(codigo, socio): el material vuelve a estar disponible.
# c.  __str__: mostrar cuántos materiales tiene la biblioteca y cuántos están prestados.
# Comportamiento esperado:
# b = Biblioteca()
# b.agregar_material(Libro("Python", "L1", "Downey"))
# s = Socio("Sofía")
# b.prestar("L1", s)
# print(b)   # Biblioteca: 1 material(es), 1 prestado(s)
# b.devolver("L1", s)
# print(b)   # Biblioteca: 1 material(es), 0 prestado(s)
class Material:
    def __init__(self, titulo, codigo):
        self.titulo = titulo
        self.codigo = codigo
        self.disponible = True


class Libro(Material):
    def __init__(self, titulo, codigo, autor):
        super().__init__(titulo, codigo)
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo} - {self.autor}"


class Revista(Material):
    def __init__(self, titulo, codigo, numero_edicion):
        super().__init__(titulo, codigo)
        self.numero_edicion = numero_edicion

    def __str__(self):
        return f"Revista: {self.titulo} - edición {self.numero_edicion}"


class Socio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__materiales_prestados = []

    def prestar_material(self, material):
        self.__materiales_prestados.append(material)

    def devolver_material(self, material):
        if material in self.__materiales_prestados:
            self.__materiales_prestados.remove(material)

    def __str__(self):
        return self.nombre


class Biblioteca:
    def __init__(self):
        self.materiales = []
        self.socios = []

    def agregar_material(self, material):
        self.materiales.append(material)

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def prestar(self, codigo, socio):
        for material in self.materiales:
            if material.codigo == codigo:
                if material.disponible:
                    material.disponible = False
                    socio.prestar_material(material)
                    print(f"{material.titulo} prestado a {socio.nombre}")
               
    def devolver(self, codigo, socio):
        for material in self.materiales:
            if material.codigo == codigo:
                material.disponible = True
                socio.devolver_material(material)
                

        

    def __str__(self):
        prestados = 0

        for material in self.materiales:
            if not material.disponible:
                prestados += 1

        return (
            f"Biblioteca: {len(self.materiales)} material(es), "
            f"{prestados} prestado(s)"
        )



b = Biblioteca()
b.agregar_material(Libro("Python", "L1", "Downey"))
s = Socio("Sofía")
b.prestar("L1", s)
print(b)   # Biblioteca: 1 material(es), 1 prestado(s)
b.devolver("L1", s)
print(b)   # Biblioteca: 1 material(es), 0 prestado(s)