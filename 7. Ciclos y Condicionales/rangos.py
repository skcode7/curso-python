for valor in range(7):
    print(valor)

print("=== Definiendo el numero inicial")
for valor in range(3, 7):
    print(valor)

print("=== Impresion con salto")
for valor in range(2, 10, 2):
    print(valor)

print("=== Para iterar una lista")
lista = [5, 3, 7, 1 ,3]
for indice in range(len(lista)):
    print("Indice = ", indice, "valor =", lista[indice])

print("=== Usando enumarate")
lista = [5, 3, 7, 1 ,3]
for indice, valor in enumerate(lista):
    print("Indice = ", indice, "valor =", valor)