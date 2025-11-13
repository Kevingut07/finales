#Pide una calificación y clasifícala en "Excelente", "Buena", "Regular" o "Mala".

calificacion = float(input("Ingresa una calificación (0-10): "))
if calificacion >= 9 and calificacion <= 10:
    print("Excelente")
elif calificacion >= 7 and calificacion < 9:
    print("Buena")
elif calificacion >= 5 and calificacion < 7:
    print("Regular")
elif calificacion >= 0 and calificacion < 5:
    print("Mala")
else:
    print("Calificación inválida")
    
    