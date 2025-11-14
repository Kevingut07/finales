#Pide las edades de tres personas y determina quién es el mayor y quién el menor.

edad1 = int(input("Ingrese la edad de la primera persona: "))
edad2 = int(input("Ingrese la edad de la segunda persona: "))
edad3 = int(input("Ingrese la edad de la tercera persona: "))

if edad1 >= edad2 and edad1 >= edad3:
    mayor = edad1
elif edad2 >= edad1 and edad2 >= edad3:
    mayor = edad2
else:
    mayor = edad3