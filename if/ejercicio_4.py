#Escribe un programa que le pida al usuario su calificación y determine si aprobó (60 o más), reprobó (menos de 60), y si es un aprobado especial (90 o más).

calificacion = float(input("Escribe tu calificación: "))

if calificacion >= 90:
    print("Aprobaste con un aprobado especial.")
elif calificacion >= 60:
    print("Aprobaste.")
elif calificacion < 60 and calificacion >= 0:
    print("Reprobaste.")
else:
    print("La calificación ingresada no es válida.")
    