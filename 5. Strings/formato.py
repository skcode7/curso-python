texto = "curso de Python 3"
resultado = texto.capitalize()
print(resultado)

resultado = texto.swapcase()
print(resultado)

resultado = texto.upper()
print(resultado)
print(resultado.isupper())
print(resultado.islower())

resultado = texto.title()
print(resultado)

resultado = texto.replace("Python", "CSS")
print(resultado)

#strip permite quitar espacios (trim)

curso = "Python"
version = "3"
resultado = "Curso de %s %s" %(curso, version)
print(resultado)

#Alternativa
resultado = "Curso de {} {}".format(curso, version)
print("OTRO = " , resultado)

resultado = "Curso de {a} {b}".format(b = version, a = curso)
print("Asignando Nombre = " , resultado)