#Pide dos números y un operador, y realiza una operación considerando casos especiales de división.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

operador = input("Ingrese el operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operador == "/":
    if num2 == 0:
        print("Error: División por cero no permitida.")
    else:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
else:
    print("Operador no válido.")