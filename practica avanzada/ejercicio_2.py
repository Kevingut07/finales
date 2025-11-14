#Pide el monto de una transferencia y el saldo disponible, y detecta si la transacción es fraudulenta.

monto_transferencia = float(input("Ingrese el monto de la transferencia: "))
saldo_disponible = float(input("Ingrese el saldo disponible: "))

if monto_transferencia > saldo_disponible:
    print("Transacción fraudulenta detectada.")
else:
    print("Transacción autorizada.")
    