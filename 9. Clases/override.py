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

    def dormir(self):
        print(self.nombre, "esta durmiendo")

firulais = Perro("firulais")
firulais.dormir()