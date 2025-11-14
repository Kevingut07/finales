#Pide una contraseña y verifica si cumple ciertos requisitos (mayúsculas, minúsculas, números).

contraseña = input("Ingrese una contraseña: ")

tiene_mayuscula = any(c.isupper() for c in contraseña)
tiene_minuscula = any(c.islower() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)

if tiene_mayuscula and tiene_minuscula and tiene_numero:
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura. Debe contener al menos una letra mayúscula, una letra minúscula y un número.")
    