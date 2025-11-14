#Pide una temperatura y verifica si está en rango de ebullición o congelación

temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

if temperatura <= 0:
    print("La temperatura está en el rango de congelación.")
elif temperatura >= 100:
    print("La temperatura está en el rango de ebullición.")
else:
    print("La temperatura está en un rango normal.")

