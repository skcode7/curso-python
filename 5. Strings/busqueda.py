mensaje = "Este es un texto extenso en cuanto a la longitud de caracteres"
resultado = mensaje.count("l")
print(resultado)

#Otra forma
resultado = "z" in mensaje
print(resultado)

#Find devuelve un entero con la posicion del primer caracter de lo buscado
resultado = mensaje.find("texto")
print(resultado)