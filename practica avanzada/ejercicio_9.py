#Escribe un programa que reciba una calificación numérica (0 a 100) y determine la categoría de la nota: "Muy deficiente" (menos de 50), "Deficiente" (50-64), "Regular" (65-74), "Buena" (75-89) y "Excelente" (90-100).

calificacion = float(input("Ingrese la calificación numérica (0-100): "))

if calificacion < 50:
    print("Categoría: Muy deficiente")
elif 50 <= calificacion < 65:
    print("Categoría: Deficiente")
elif 65 <= calificacion < 75:
    print("Categoría: Regular")
elif 75 <= calificacion < 90:
    print("Categoría: Buena")
else:
    print("Categoría: Excelente")
    