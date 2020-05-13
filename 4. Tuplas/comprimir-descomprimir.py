tupla = (3,5,1)
uno, dos, tres = tupla
print(uno)
print(dos)
print(tres)

##Para evitar errores se puede utilizar el * (en cualquier posicion)
tupla = (3,5,1, 45, 12 , 98)
uno, *dos, tres = tupla
print("*")
print(uno)
print(dos)
print(tres)

print("================ ZIP")
tupla = (3,5,1, 45, 12 , 98)
lista = [33, 55, 1, 2]
tupla2 = (4, 5 , 61, 1)

resultado = zip(tupla, lista, tupla2)
resultado = list(resultado)
print(resultado)

print("====================== Desempaquetado")
tupla = (10, 20, 30, 40, 50)

##con lineas independientes
primero = tupla[0]
segundo = tupla[1]
ultimo = tupla[-1]

##en una sola linea
primero, segundo, ultimo = tupla[0], tupla[1], tupla[-1]

##directo con la tupla
primero, segundo, _, _, ultimo = tupla

##usando *
tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400)
primero, segundo, *_, ultimo = tupla
print(primero, segundo, ultimo)