calificacion = int(input("Ingrese calificacion: "))
color = None

if calificacion > 7:
    color = "verde"
else:
    color = "rojo"
print(calificacion, color)

#reduciendo lineas de codigo
calificacion = int(input("Ingrese calificacion: "))
color = "verde" if calificacion > 7 else "rojo"
print(calificacion, color)