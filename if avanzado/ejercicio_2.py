#Pide peso y altura, calcula el IMC y clasifícalo en "Bajo peso", "Normal", "Sobrepeso" o "Obesidad"

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 24.9:
    clasificacion = "Normal"
elif 25 <= imc < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"
    
print(f"Su IMC es: {imc:.2f}, Clasificación: {clasificacion}")

