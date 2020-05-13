lista = ["Curso", "CodigoFacilito"]
tupla = ("Intro", "Basico", "Avanzado")

print(lista)
print(tupla)

nueva_lista = list(tupla)
nueva_tupla = tuple(lista)
print(nueva_tupla)
print(nueva_lista)

##Los strings son listas
print("========== STRINGS")
mensaje = "Curso gratuito"
nueva_lista = list(mensaje)
print(nueva_lista)