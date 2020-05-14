def saludar():
    print("Hola mundo")

def mensaje(nombre):
    return "Hola {}, bienvenido al curso de Python".format(nombre)

#recibir varios parametros
def suma(val1, val2, val3):
    return val1 + val2 + val3

#retornar varios valores
def obtener_curso():
    return "Curso de Python", "Basico", 3.6

saludar()
print(mensaje("CHARLY"))
print("Suma = " , suma(3, 5, 7))
curso, nivel, version = obtener_curso()
print(curso, nivel, version)