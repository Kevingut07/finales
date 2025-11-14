#Pide un puntaje de examen y determina en qué rango cae (por ejemplo, A, B, C, D, o F).

puntaje = float(input("Ingrese el puntaje del examen (0-100): "))

if 80 <= puntaje <= 100:
    print("Calificación: A")
elif 70 <= puntaje < 80:
    print("Calificación: B")
elif 60 <= puntaje < 70:
    print("Calificación: C")
elif 50 <= puntaje < 60:
    print("Calificación: D")
elif 0 <= puntaje < 50:
    print("Calificación: F")
else:
    print("Puntaje inválido. Ingrese un valor entre 0 y 100.")
    
    