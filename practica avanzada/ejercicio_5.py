#Pide dos números y determina si son pares o impares y si uno es múltiplo del otro

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 % 2 == 0:
    print(f"El número {num1} es par.")
else:
    print(f"El número {num1} es impar.")
    
if num2 % 2 == 0:
    print(f"El número {num2} es par.")
else:
    print(f"El número {num2} es impar.")
    
    
if num1 % num2 == 0:    
    print(f"El número {num1} es múltiplo de {num2}.")
elif num2 % num1 == 0:
    print(f"El número {num2} es múltiplo de {num1}.")
else:
    print("Ninguno de los números es múltiplo del otro.")

