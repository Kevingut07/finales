#Pide el precio de un producto y si es esencial o no, y aplica IVA según el tipo.

precio_producto = float(input("Ingrese el precio del producto: "))
esencial = input("¿El producto es esencial? (s/n): ")

if esencial == 's':
    iva = 0.04
else:
    iva = 0.16  
    
precio_final = precio_producto + (precio_producto * iva)

print(f"El precio final del producto con IVA es: ${precio_final:.2f}")