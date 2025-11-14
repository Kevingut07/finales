#Pide la edad y determina si la persona puede votar, y si es obligatorio (entre 18 y 70años).

edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("No puede votar.")
elif 18 <= edad <= 70:
    print("Puede votar y es obligatorio.")
    
    