#Pide un número y determina si es positivo, negativo o cero.

num = float(input("Escribe un numero: "))
if num > 0:
    print(f"El numero {num} es positivo.")
elif num < 0:
    print(f"El numero {num} es negativo.")
else:
    print("El numero es cero.")