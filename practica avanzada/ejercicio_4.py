#Pide un día de la semana y determina si es fin de semana o día laboral.

dia_semana = input("Ingrese un día de la semana: lunes, martes, miércoles, jueves, viernes, sábado, domingo: ")

if dia_semana in ['sábado', 'domingo']:
    print("Es fin de semana.")
elif dia_semana in ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']:
    print("Es un día laboral.") 