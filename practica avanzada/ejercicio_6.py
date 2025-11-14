#Un supermercado ofrece descuentos en función de la hora de compra. Si la compra es antes de las 12:00 p.m., se aplica un 10% de descuento. Si la compra es después de las 6:00 p.m., el descuento es del 20%. En otros horarios, no hay descuento. Escribe un programa que determine el descuento aplicable y el total a pagar.

hora_compra = float(input("Ingrese la hora de compra en formato 24 horas (por ejemplo, 14.30 para 2:30 p.m.): "))
monto_compra = float(input("Ingrese el monto de la compra: "))

if hora_compra < 12.00:
    descuento = 0.10
    monto_final = monto_compra * (1 - descuento)
    print(f"Se aplica un descuento del 10%. Monto a pagar: ${monto_final:.2f}")
elif hora_compra > 18.00:
    descuento = 0.20
    monto_final = monto_compra * (1 - descuento)
    print(f"Se aplica un descuento del 20%. Monto a pagar: ${monto_final:.2f}")
else:
    monto_final = monto_compra
    print(f"No se aplica descuento. Monto a pagar: ${monto_final:.2f}")
    
    