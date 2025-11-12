#Pide tres números y muestra si son todos pares, todos impares, o hay mezcla.

num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))
num3 = int(input("Escribe el tercer numero: "))

if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
    print("Los tres numeros son pares.")
elif num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0:
    print("Los tres numeros son impares.")
else:
    print("Hay una mezcla de numeros pares e impares.")