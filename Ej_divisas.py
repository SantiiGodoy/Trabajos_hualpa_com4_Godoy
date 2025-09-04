#Ejercicio 7: Conversión de divisas. 
# Un programa que lea un monto en dólares y lo convierta a pesos colombianos, 
# argentinos y euros usando tasas de cambio fijas definidas en el código.
print("")
print(" == CONVERSIÓN DE DIVISAS == ")
print("")

USD_COL = 4031.0
USD_ARG = 1351.0
USD_EUR = 0.8626

ingreso_usd = float(input("Ingrese su monto en dólares(USD): "))

pesos_COL = ingreso_usd * USD_COL
pesos_ARG = ingreso_usd * USD_ARG
euros = ingreso_usd * USD_EUR

print(f"\nDinero ingresado: {ingreso_usd}$USD\nConvertidos a: ")
print(f"{pesos_COL:,} pesos colombianos ")
print(f"{pesos_ARG:,} pesos argentinos ")
print(f"{euros:,.2f} euros")
