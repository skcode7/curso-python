class Circulo:
    pi = 3.14159265

    def __init__(self, radio):
        self.radio = radio

circulo_a = Circulo(10)
circulo_b = Circulo(20)

print(circulo_a.radio)
print(circulo_b.radio)

print("si se cambia el valor de radio en b, solo afecta a la instacia")
circulo_b.radio = 100

print(circulo_a.radio)
print(circulo_b.radio)

print("Las variables de clase se pueden utilizar sin instanciar la clase")
print(Circulo.pi)