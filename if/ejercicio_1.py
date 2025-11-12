# Escribe un programa que le pida al usuario un número entero y determine si es par o impar

num = int(input("Escribe un numero para determinar si es par o impar: "))

if num % 2 == 0:
    print(f"El numero {num} es par")
else:
    print(f"El numero {num} es impar")

