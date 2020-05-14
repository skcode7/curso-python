numeros = [1, 2, 3, 4, 5 , 6]
for numero in numeros:
    print(numero)


#en diccionarios se itera las llasves
diccionario = {"a":1, "b":2, "c":3, "d":4, "e":6}
for llave in diccionario:
    print(llave)


#iterar objeto con objetos
print("==== Doble")
valores = ((10, 20, 30), ["hola", "chao", " "], (True, False, 0))
for valor1, valor2, valor3 in valores:
    print(valor1, valor2, valor3)