#Pide el número de días de retraso en la devolución de un libro y calcula la multa.

dias_retraso = int(input("Ingrese el número de días de retraso en la devolución del libro: "))

if dias_retraso <= 0:
    multa = 0
elif 1 <= dias_retraso <= 5:
    multa = dias_retraso * 0.50
elif 6 <= dias_retraso <= 10:
    multa = dias_retraso * 1.00
else:
    multa = dias_retraso * 2.00

print(f"La multa por la devolución tardía es: ${multa:.2f}")
