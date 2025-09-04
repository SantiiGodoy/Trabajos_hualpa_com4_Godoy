consumo_auto = 8 / 100

km_recorrer = float(input("Ingrese la distancia en km que desea recorrer: "))
precio_gasolina = float(input("Ingrese el precio de la gasolina por litros: "))

litros_necesarios = km_recorrer * consumo_auto
costo = precio_gasolina * litros_necesarios
demora_viaje = km_recorrer / 90

print(f"Los litros que se necesitan son {litros_necesarios:.2f} litros ")
print(f"El costo total del viaje es de ${costo:.2f} ")
print(f"Si manejan a 90km/h se calcula una demora de {demora_viaje:.2f}hs ")
