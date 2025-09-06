print("")
nombre_completo = input("Ingrese su nombre completo: ").title()
dni = (input("Ingrese su dni sin puntos: "))
edad_paciente = int(input("Ingrese su edad: "))
obra_social = input ("Tiene obra social? (si/no) ")
prioridad_medica = int(input("1.emergencia\n2.urgente\n3.control\nSu elección: "))
prioridad_i = [1, 2, 3]
turno = ""

def validar_dni (dni):
    dni_validado = dni if (len(dni)==8) else "DNI invalido"
    if dni_validado == dni: return dni_validado

if prioridad_medica == prioridad_i[0]:
    turno = "Guardia"
elif prioridad_medica == prioridad_i[1]:
    if obra_social == "si":
        turno = "Turno en menos de 24hs. "
    else: turno = "Turno en 48hs. "
elif prioridad_medica == prioridad_i[2]:
    if edad_paciente > 65:
        turno = "Turno preferencial en 72hs. "
    else: turno = "Turno normal en 7 días. "

print(f"Paciente: {nombre_completo}")
print(f"DNI: {validar_dni(dni)}")
print(f"Edad: {edad_paciente}")
print(f"Turno: {turno}")
