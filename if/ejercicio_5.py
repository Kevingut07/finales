#Escribe un programa que le pida al usuario dos números y un operador (+, -, *, /) y realice la operación correspondiente.

num1 = float(input("Escribe el primer numero: "))
num2 = float(input("Escribe el segundo numero: "))
operador = input("Escribe el operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es: {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} es: {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} es: {resultado}")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operador no válido. Por favor, utiliza +, -, * o /.")