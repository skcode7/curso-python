def tabla_multiplicar(numero, maximo=10):
    for factor in range(1, maximo+1):
        yield numero * factor

#multiples parametros
def tabla_multiplicar_txt(numero, maximo=10):
    for factor in range(1, maximo+1):
        yield numero * factor, numero, factor

for resultado in tabla_multiplicar(7):
    print(resultado)
    
for resultado, numero, factor in tabla_multiplicar_txt(7, 20):
    print(numero, "*", factor, "=", resultado)