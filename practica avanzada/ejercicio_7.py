#Escribe un programa que pida un número de mes (1 para enero, 2 para febrero, etc.) y determine en qué trimestre del año se encuentra.

mes = int(input("Ingrese el número del mes (1-12): "))
if 1 <= mes <= 3:
    print("El mes corresponde al primer trimestre del año.")
elif 4 <= mes <= 6:
    print("El mes corresponde al segundo trimestre del año.")
elif 7 <= mes <= 9:
    print("El mes corresponde al tercer trimestre del año.")
elif 10 <= mes <= 12:
    print("El mes corresponde al cuarto trimestre del año.")
else:
    print("Número de mes inválido. Por favor ingrese un número entre 1 y 12.")