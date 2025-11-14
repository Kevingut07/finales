#Una empresa de alquiler de autos permite alquilar vehículos solo a personas mayores de 21 años. Sin embargo, si la persona tiene entre 21 y 25 años, se le cobra un cargo adicional del 15%. Si es mayor de 25, no se cobra ningún cargo adicional. Escribe un programa que determine si alguien puede alquilar un auto y el costo adicional si aplica.

edad = int(input("Ingrese su edad: "))

if edad < 21:
    print("No puede alquilar un auto.")
elif 21 <= edad <= 25:
    print("Puede alquilar un auto, pero se le cobrará un cargo adicional del 15%.")
else:
    print("Puede alquilar un auto sin cargo adicional.")
