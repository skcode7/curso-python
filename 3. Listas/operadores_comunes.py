lista = [8.17, 90, 1, 5, 44, 1.32]
print(lista)
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

print("Minimo = ", min(lista))
print("Maximo = ", max(lista))

print("Longitud = " , len(lista))

##Buscar elemento en lista
resultado = 8 in lista
print(resultado)

print("Indice = " , lista.index(5))