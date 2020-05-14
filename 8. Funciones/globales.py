animal = "Leon"

def mostrar_animal():
    print("Funcion", animal)

animal = "Leon"
def mostrar_animal2():
    animal = "Perro"    #se cambia el valor en el namespace de la funcion
    print("Funcion", animal)

animal = "Leon"
def mostrar_animal3():
    global animal
    animal = "Perro"    #se cambia el valor global
    print("Funcion", animal)



mostrar_animal()
print(animal)

mostrar_animal2()
print(animal)

mostrar_animal3()
print(animal)