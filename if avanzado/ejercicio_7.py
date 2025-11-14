#Pide una temperatura en grados Celsius y convierte a Fahrenheit o Kelvin.

temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
unidad_destino = input("Ingrese la unidad a convertir (F para Fahrenheit, K para Kelvin): ")

if unidad_destino=='F':
    temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
    print(f"La temperatura en Fahrenheit es: {temperatura_fahrenheit:.2f} °F")
elif unidad_destino=='K':
    temperatura_kelvin = temperatura_celsius + 273.15
    print(f"La temperatura en Kelvin es: {temperatura_kelvin:.2f} K")
else:
    print("Unidad no válida. Por favor ingrese 'F' o 'K'.")
    
    