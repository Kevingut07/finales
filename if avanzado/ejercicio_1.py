#Pide el número de horas trabajadas y calcula el salario con 50% más para horas extra.


horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
tarifa_hora = float(input("Ingrese la tarifa por hora: "))

if horas_trabajadas > 44:
    horas_extra = horas_trabajadas - 44
    salario = (44 * tarifa_hora) + (horas_extra * tarifa_hora * 1.5)
else:
    salario = horas_trabajadas * tarifa_hora
    
print(f"El salario total es: {salario:.2f}")
