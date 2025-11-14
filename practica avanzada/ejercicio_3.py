#Pide un tipo de sangre y determina a qué grupos puede donar y recibir

tipo_sangre = input("Ingrese su tipo de sangre (A, B, AB, O): ")

if tipo_sangre == 'A':
    puede_donar = ['A', 'AB']
    puede_recibir = ['A', 'O']
elif tipo_sangre == 'B':
    puede_donar = ['B', 'AB']
    puede_recibir = ['B', 'O']
elif tipo_sangre == 'AB':
    puede_donar = ['AB']
    puede_recibir = ['A', 'B', 'AB', 'O']
elif tipo_sangre == 'O':
    puede_donar = ['A', 'B', 'AB', 'O']
    puede_recibir = ['O']
else:
    print("Tipo de sangre inválido.")

print(f"Puede donar a los tipos de sangre: {', '.join(puede_donar)}")
print(f"Puede recibir de los tipos de sangre: {', '.join(puede_recibir)}")