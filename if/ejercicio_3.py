#Crea un programa que pida la edad de una persona y determine si es un niño (0-12 años), un adolescente (13-17 años), un adulto (18-64 años) o un adulto mayor (65 años o más).

edad = int(input("Escribe tu edad: "))

if edad >= 0 and edad <= 12:
    print("Eres un niño.")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente.")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto.")
elif edad >= 65:
    print("Eres un adulto mayor.")
else:
    print("La edad ingresada no es válida.")
    
    
    