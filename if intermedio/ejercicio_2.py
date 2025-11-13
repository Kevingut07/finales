#Pide dos números y determina si el primero es múltiplo del segundo.

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num2 != 0:
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}")
    else:
        print(f"{num1} no es múltiplo de {num2}")
else:
    print("Error: No se puede dividir por cero.")
    