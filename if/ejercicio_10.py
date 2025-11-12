#Pide la edad y determina el descuento: 50% si es menor de 12, 20% si es mayor de 65, y sin descuento para los demás.

edad = int(input("Escribe tu edad: "))
if edad < 12:
    print("Tienes un descuento del 50%.")
elif edad > 65:
    print("Tienes un descuento del 20%.")
else:
    print("No tienes descuento.")
    
    