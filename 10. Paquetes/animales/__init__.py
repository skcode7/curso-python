#Para definir un paquete debe tener el archivo init
print("Mensaje de init")

#se pueden exponer clases de los modulos
from .aves import Pinguino
from .felinos import Tigre

#se pueden generar instancias
mi_tigre = Tigre()