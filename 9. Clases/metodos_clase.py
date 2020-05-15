class Circulo:
    pi = 3.14159265

    @classmethod
    def area(cls, radio):
        return cls.pi * radio**2


resultado = Circulo.area(100)
print(resultado)