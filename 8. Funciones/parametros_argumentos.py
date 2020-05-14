def crear_usuario(nombre, apellido, edad):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{} {}".format(nombre, apellido),
        'edad': edad
    }

#Valor default en parametros
def crear_usuario2(nombre, apellido, edad=99):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{} {}".format(nombre, apellido),
        'edad': edad
    }

#Llamada con nombre de parametro
def crear_usuario3(nombre="", apellido="", edad=99):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{} {}".format(nombre, apellido),
        'edad': edad
    }

usuario = crear_usuario("Carlos", "Encalada", 36)
print(usuario)

usuario = crear_usuario2("Carlos", "Encalada")
print(usuario)

usuario = crear_usuario3(apellido="Encalada")
print(usuario)