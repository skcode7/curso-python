from calculadora import *   #importa todos los elementos
from calculadora import division, producto   #importa el elemento especifico
from calculadora import resta as r   #importa el elemento especifico y le asigna un alias

resultado = r(4, 6)
print(resultado)