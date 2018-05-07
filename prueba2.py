#import clase_prueba

class Casa:
    def __init__(self, pisos = None, habitaciones = None, metros = None):
        # Datos usuario/host
        self.pisos = pisos
        self.habitaciones = habitaciones
        self.metros = metros


    def get_altura(self):
        return self.pisos

    def get_habitaciones(self):
        return self.habitaciones

    def get_metros(self):
        return self.metros

c = Casa()
c.pisos = 2
c.habitaciones = 3
c.metros = 100
print([c.pisos,c.habitaciones,c.metros])


print("a")
print("a")
print("a")
print("a")
print("a")