#Pide el total de la compra e indica si tiene 10% de descuento si es mayor a 100000 COP

total_compra = float(input("Escribe el total de la compra en COP: "))
if total_compra > 100000:
    descuento = total_compra * 0.10
    total_con_descuento = total_compra - descuento
    print(f"Tienes un descuento del 10%. El total a pagar es: {total_con_descuento} COP")
else:
    print(f"No tienes descuento. El total a pagar es: {total_compra} COP")
    
    