#Escribe un programa que le pida al usuario tres números y determine cuál es el mayor.

num1 = float(input("Escribe el primer numero: "))
num2 = float(input("Escribe el segundo numero: "))
num3 = float(input("Escribe el tercer numero: "))

if num1 > num2 and num1 > num3:
    print(f"El numero mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El numero mayor es: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"El numero mayor es: {num3}")
else:
    print("Hay numeros iguales entre si.")    