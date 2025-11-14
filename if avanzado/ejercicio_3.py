#Pide un mes y determina si está dentro del ciclo escolar o en vacaciones.

mes = input("Ingrese el mes (en minúsculas): ")
meses_ciclo_escolar = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "agosto", "septiembre", "octubre", "noviembre"]

if mes in meses_ciclo_escolar:
    print("El mes está dentro del ciclo escolar.")
else:
    print("El mes está en vacaciones.")
    
    