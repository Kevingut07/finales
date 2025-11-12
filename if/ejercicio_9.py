#Pide un número y muestra la raíz cuadrada si es positivo. Si es negativo, muestra un mensaje diciendo que no tiene raíz real.

import math

num = float(input("Escribe un numero: "))
if num >= 0:
    raiz = math.sqrt(num)
    print(f"La raiz cuadrada de {num} es {raiz}")
else:
    print("El numero no tiene raiz real.")