#map permite aplicar una funcion a los items de un objeto iterable (listas, tuplas, etc.)
def cuadrado(numero):
    return numero * numero

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)
lista_resultado = list(resultado)
print(lista_resultado)

#utilizando lambda
lista = [1,2,3,4,5]
resultado = map(lambda numero: numero * numero , lista)

lista_resultado = list(resultado)
print(lista_resultado)