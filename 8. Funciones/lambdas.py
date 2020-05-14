def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

#lambda = funcion anonima
conversor = lambda grados : grados * 1.8 + 32

#asignacion de funcion a una variable
funcion_variable = centigrados_a_farhenheit
resultado = funcion_variable(37.8)
print(resultado)

resultado = conversor(16)
print(resultado)