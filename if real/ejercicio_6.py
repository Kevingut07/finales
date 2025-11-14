#Pide cinco calificaciones y calcula el promedio, luego muestra el nivel de desempeño (bajo, medio, alto).

calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))
calificacion4 = float(input("Ingrese la cuarta calificación: "))
calificacion5 = float(input("Ingrese la quinta calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

if promedio < 2.9:
    nivel = "Bajo"
elif 2.9 <= promedio < 3.9:
    nivel = "Medio"
else:
    nivel = "Alto"