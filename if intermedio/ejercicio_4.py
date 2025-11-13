#Pide una velocidad y clasifícala en "Baja", "Normal" o "Alta".

velocidad = float(input("Ingresa la velocidad en km/h: "))

if velocidad < 40:
    print("Su velocidad es Baja")
elif velocidad >= 40 and velocidad <= 80:
    print("Su velocidad es Normal")
else:
    print("Su velocidad es Alta")
    
    