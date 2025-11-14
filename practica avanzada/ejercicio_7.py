#Pide calificaciones de tareas, proyectos y exámenes y calcula la nota final.

tarea1 = float(input("Ingrese la calificación de la tarea 1: "))
proyecto = float(input("Ingrese la calificación del proyecto: "))
examen_final = float(input("Ingrese la calificación del examen final: "))

nota_final = (tarea1 * 0.3) + (proyecto * 0.3) + (examen_final * 0.4)
print(f"La nota final es: {nota_final:.2f}")

if nota_final < 2.9:
    print("Desempeño: Insuficiente")
elif 2.9 <= nota_final < 3.9:
    print("Desempeño: Aceptable")
else:
    print("Desempeño: Excelente")
    
    