
d_km = float(input("Ingrese la distancia recorrida (en km): "))
pr_l = float(input("Ingrese el precio de la gasolina (por litros): "))

l_necesarios = (d_km * 8) / 100
costo_viaje = (l_necesarios * pr_l)
horas_viaje = d_km / 90

print("En base a los datos proporcionados:")
print(f'Se necesitan {l_necesarios}litros para realizar el viaje')
print(f'El viaje tiene un costo de ${costo_viaje}')
print(f'Con una velocidad constante de 90km/h, el viaje tardará {round(horas_viaje, 2)} horas en completarse')
print("\n\n")


