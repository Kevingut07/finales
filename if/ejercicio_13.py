#Pide dos letras e indica si son iguales o cuál es mayor alfabéticamente.
letra1 = input("Escribe la primera letra: ")
letra2 = input("Escribe la segunda letra: ")

if letra1 == letra2:
    print("Las letras son iguales.")
elif letra1 > letra2:
    print(f"La letra {letra1} es mayor alfabéticamente que la letra {letra2}.")
elif letra2 > letra1:
    print(f"La letra {letra2} es mayor alfabéticamente que la letra {letra1}.")
else:
    print("Error en la comparación de letras.")
    