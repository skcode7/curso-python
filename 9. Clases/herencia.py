class Animal:
    def comer(self):
        print("Estoy comiendo")
    def dormir(self):
        print("Estoy durmiendo")

class Perro(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Estoy ladrando")

firulais = Perro("firulais")

firulais.comer()
firulais.dormir()
firulais.ladrar()