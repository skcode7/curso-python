class Usuario:
    def __init__(self, username='', correo='', nombre=''):
        self.username = username
        self.correo = correo
        self.nombre = nombre        

    def saluda(self):   #se pueden agregar N parametros
        return "Hola, soy " + self.nombre

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)

codi = Usuario("Charly", "sk@mail.com", "Carlos")
facilito = Usuario('Otro')

print(type(codi))

print(codi.saluda())

