#Pide una temperatura y clasifícala como "Muy frío", "Frío", "Tibio", "Caliente", o "Muy caliente".

temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

if temperatura < 0:
    print("Muy frío")
elif 0 <= temperatura < 15:
    print("Frío")
elif 15 <= temperatura < 25:
    print("Tibio")
elif 25 <= temperatura < 35:
    print("Caliente")
else:
    print("Muy caliente")