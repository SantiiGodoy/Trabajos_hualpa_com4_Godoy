monto_prestamo = float(input("Ingrese el monto del prestamo: "))
cant_meses = int(input("Ingrese la cantidad de meses a pagar: "))
INTERES_FIJO = 2 / 100

monto_total = monto_prestamo * (1 + (INTERES_FIJO))**cant_meses

cuota_mensual = (monto_prestamo * INTERES_FIJO) / (1 - (1 + INTERES_FIJO)**(-cant_meses))
print(f"El monto total a devolver es de ${round(monto_total, 3)}")
print(f"El valor de cada cuota mensual es de: ${round(cuota_mensual, 2)}")