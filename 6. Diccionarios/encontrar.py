diccionario = {"a":1, "b":2, "c":3, "a":4}

resultado = "z" in diccionario
print(resultado)        #condicionando el resultado se podria evitar el error Key no encontrado

#Otra alternativa es con Get
resultado = diccionario.get("z", "La llave no existe")
print(resultado)

#se puede setear un valor a la llave que no existe
resultado = diccionario.setdefault("z", {})
print(resultado)
print(diccionario)