#Pide el ingreso anual y calcula el impuesto basado en tramos de ingresos

ingreso_anual = float(input("Ingrese su ingreso anual: "))

if ingreso_anual <= 10000:
    impuesto = 0
elif 10001 <= ingreso_anual <= 30000:
    impuesto = ingreso_anual * 0.15
elif 30001 <= ingreso_anual <= 100000:
    impuesto = ingreso_anual * 0.25
else:
    impuesto = ingreso_anual * 0.35
    
print(f"El impuesto a pagar es: {impuesto:.2f}")