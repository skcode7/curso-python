class Animal:
    def comer(self):
        print("Estoy comiendo")
    def dormir(self):
        print("Estoy durmiendo")

class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_adopcion = fecha

class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Estoy ladrando")

firulais = Perro("firulais")
firulais.fecha_adopcion("Hoy")
print(firulais.fecha_adopcion)