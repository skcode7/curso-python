titulo = "Curso de Python 3"

for caracter in titulo:
    if caracter == "P":
        break       #termina la ejecucion del lazo
    print(caracter)

for caracter in titulo:
    if caracter == "P":
        continue       #omite el caracter
    print(caracter)