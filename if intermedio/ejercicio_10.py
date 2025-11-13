#Pide una letra y determina si es vocal o consonante.

letra = input("Ingresa una letra: ")

if letra in 'aeiou' and len(letra) == 1:
    print(f"La letra '{letra}' es una vocal.")
else:
    print(f"La letra '{letra}' es una consonante.")