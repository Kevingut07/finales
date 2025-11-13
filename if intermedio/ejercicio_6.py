#Calcula el promedio de tres notas y determina si el estudiante aprueba o reprueba (mínimo 60).

nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 60:
    print(f"El estudiante aprueba con un promedio de {promedio:.2f}")
else:
    print(f"El estudiante reprueba con un promedio de {promedio:.2f}")