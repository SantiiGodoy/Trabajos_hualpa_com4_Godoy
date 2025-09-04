#Ejercicio 6: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales. 
# 30% de la calificación del examen final. 
# 15% de la calificación de un trabajo final.

parcial1 = float(input("Parcial 1: "))
parcial2 = float(input("Parcial 2: "))
parcial3 =  float(input("Parcial 3: "))
print("")
examen_final = float(input("Examen final: "))
trabajo_final = float(input("Trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
total = 0.55 * promedio_parciales + 0.30 * examen_final + 0.15 *trabajo_final

print(f"La calificacion de los parciales es {promedio_parciales}")
print(f"La calificacion total es {total} ")



