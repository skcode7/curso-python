#todas las clases heredan de Object
#con __ se trabaja con los metodos de Object
#al sobre-escribir str se modifica para que imprima el nombre en lugar de la direccion de memoria

class Gato():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

pato = Pato("Lucas")
gato = Gato("Silvestre")

print(pato)
print(gato)

#con __dict se puede obtener un diccionario con los atributos
pato.edad = 4
print(pato.__dict__)
print(gato.__dict__)
