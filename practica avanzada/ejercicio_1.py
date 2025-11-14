#Pide un código de descuento y aplica un descuento específico si es válido.

codigo_descuento = input("Ingrese el código de descuento: DESC10 o DESC20: ")

if codigo_descuento == "DESC10":
    descuento = 0.10
    print(f"Descuento aplicado: {descuento*100:.0f}%")
elif codigo_descuento == "DESC20":
    descuento = 0.20
    print(f"Descuento aplicado: {descuento*100:.0f}%")
else:
    print("Código de descuento no válido. No se aplicó ningún descuento.")