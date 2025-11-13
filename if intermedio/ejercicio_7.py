#Pide dos números y muestra cuál está más cerca de 100.

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

distancia_num1 = abs(100 - num1)
distancia_num2 = abs(100 - num2)

if distancia_num1 < distancia_num2:
    print(f"El número {num1} está más cerca de 100.")
elif distancia_num2 < distancia_num1:
    print(f"El número {num2} está más cerca de 100.")
else:
    print("Ambos números están a la misma distancia de 100.")