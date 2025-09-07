print("")

nombre_completo = input("Ingrese su nombre completo: ").title()
cuit_user = input("Ingrese su número de CUIT: ").strip().split()
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales: "))
antiguedad = int(input("Ingrese su antiguedad(en años): "))
historial_credit = input("Ingrese su historial:\n-bueno\n-regular\n-malo\nEscriba su respuesta:").lower()
opciones = ["bueno", "regular", "malo"]


def cuit_v (cuit_user):
    inicio_valido = ["20", "23", "24", "27"]
    if len(cuit_user) != 3:
        return "El CUIT es inválido. "
    if cuit_user[0] not in inicio_valido:
        return "CUIT inválido.(inicio incorrecto) "
    if len(cuit_user[1]) != 8 or not cuit_user[1].isdigit():
        return "CUIT inválido. "
    if len(cuit_user[2]) != 1 or not cuit_user [2].isdigit():
        return "CUIT inválido.(dígito final incorrecto) "
    return f"{cuit_user[0]}-{cuit_user[1]}-{cuit_user[2]}"


def user (ingresos, antiguedad, historial):
    if historial not in opciones:
        return "Historial no válido. "
    if ingresos < 200000 or historial_credit == "malo":
        return "Rechazado. "
    if ingresos >= 200000 and antiguedad >= 2:
        if historial == "bueno":
            return "$3.000.000"
    elif historial == "regular":
        return "$500.000"
    else:
        return "$500.000"


print(f"Cliente: {nombre_completo}")
print(f"CUIT: {cuit_v(cuit_user)}")
print(f"Ingresos: ${ingresos_mensuales}")
print(f"Antiguedad: {antiguedad} años")
print(f"Historial: {historial_credit}")
print(f"Monto aprobado: {user(ingresos_mensuales, antiguedad, historial_credit)}")