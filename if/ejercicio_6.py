#Pide la edad de una persona y determina si es mayor o menor de edad.

edad = int(input("Escribe tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 0 and edad < 18:
    print("Eres menor de edad.")
else:
    print("La edad ingresada no es válida.")