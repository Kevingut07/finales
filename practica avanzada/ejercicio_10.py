#Crea un programa que pida la edad de una persona y determine su fase de vida: "Infancia" (0-12), "Adolescencia" (13-17), "Adultez" (18-59) y "Vejez" (60 o más).

edad = int(input("Ingrese su edad: "))

if 0 <= edad <= 12:
    print("Fase de vida: Infancia")
elif 13 <= edad <= 17:
    print("Fase de vida: Adolescencia")
elif 18 <= edad <= 59:
    print("Fase de vida: Adultez")
else:
    print("Fase de vida: Vejez")