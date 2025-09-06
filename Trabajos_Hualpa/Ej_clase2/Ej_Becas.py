print("")

nombre_usuario = input("Ingrese su nombre: ")
edad_usuario = int(input("Ingrese su edad: "))
promedio = float(input("Ingrese su promedio general: "))
ingresos_familiares = float(input("Digite sus ingresos familiares mensuales: "))
beca = ""

if promedio < 6:
    beca = "Rechazado"
elif promedio >= 6 and promedio < 10:
    if ingresos_familiares < 300000:
        beca = "Beca completa"
    elif ingresos_familiares >= 300000 and ingresos_familiares < 600000:
        beca = "Media beca"
elif ingresos_familiares > 600:
    beca = "Rechazada"
else:
    print("Promedio inválido.")

print(f"{nombre_usuario}, de {edad_usuario} años\nPromedio {round(promedio, 1 )}")
print(f"Ingresos: ${ingresos_familiares}\nResultados: {beca}")
