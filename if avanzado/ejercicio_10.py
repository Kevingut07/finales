#Pide un usuario y contraseña y verifica si coinciden con valores predeterminados.

usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("Ingrese el usuario: ")
contrasena = input("Ingrese la contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
    
    
    