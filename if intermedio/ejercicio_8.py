#Pide tres lados y verifica si pueden formar un triángulo.

lado1 = float(input("Ingresa el primer lado: "))
lado2 = float(input("Ingresa el segundo lado: "))
lado3 = float(input("Ingresa el tercer lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Los lados pueden formar un triángulo.")
else:
    print("Los lados no pueden formar un triángulo.")