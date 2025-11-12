#Pide un número y verifica si está entre 1 y 100.

num = float(input("Escribe un numero: "))
if 1 <= num <= 100:
    print(f"El numero {num} está entre 1 y 100.")
else:
    print(f"El numero {num} no está entre 1 y 100.")