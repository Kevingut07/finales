#Pide un número entre 1 y 7 y muestra el día correspondiente.

numero_dia = int(input("Ingrese un número entre 1 y 7: "))

if numero_dia == 1:
    print("Lunes")
elif numero_dia == 2:
    print("Martes")
elif numero_dia == 3:
    print("Miércoles")
elif numero_dia == 4:
    print("Jueves")
elif numero_dia == 5:
    print("Viernes")
elif numero_dia == 6:
    print("Sábado")
elif numero_dia == 7:
    print("Domingo")    
else:
    print("Número inválido. Por favor ingrese un número entre 1 y 7.")
    
    