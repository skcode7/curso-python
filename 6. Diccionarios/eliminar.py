diccionario = {"a":1, "b":2, "c":3, "d":21, "e":81, "f":5, "g":32}
print(diccionario)
print(len(diccionario))

del diccionario["a"]
print(diccionario)
print(len(diccionario))

diccionario.pop("b")
print(diccionario)
print(len(diccionario))

#Para eliminar todos los items
diccionario = {}
print(diccionario)
print(len(diccionario))

#Otra opcion es con clear