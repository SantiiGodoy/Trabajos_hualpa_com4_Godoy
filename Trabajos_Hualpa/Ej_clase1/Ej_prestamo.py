
monto = float(input("Escriba el monto solicitado: "))

interes_fijo = 0.02
meses = 12

total = monto * (1 + interes_fijo * 12)
pagar_mensual = total / meses 

print(f"El monto total a devolver es de ${total:.2f} ")
print(f"La cuota mensual es de ${pagar_mensual:.2f} ")
