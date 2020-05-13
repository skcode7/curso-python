lenguajes = "Python; Java; C; C++; Ruby; JS; PHP; C#"
resultado = lenguajes.split()
print(resultado)

#definir separador
separador = "; "
resultado = lenguajes.split(separador)
print("Lista separada ", resultado)

#Pasar de lista a string
nuevo_string = "_".join(resultado)
print(nuevo_string)

#Separar lineas por salto de pagina
texto = """Este es un texto
con saltos
de linea"""
resultado = texto.splitlines()
print(resultado)