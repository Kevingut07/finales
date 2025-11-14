#Pide la categoría del cliente y calcula el descuento en base a la categoría.

categoria = input("Ingrese la categoría del cliente (A, B, C): ")

if categoria == "A":
    descuento = 0.10
elif categoria == "B":
    descuento = 0.05
elif categoria == "C":
    descuento = 0.02
else:
    descuento = 0.0
    
print(f"El descuento aplicado es: {descuento*100:.0f}%")

