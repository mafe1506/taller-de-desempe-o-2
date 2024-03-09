nota_taller1 = float(input("Ingrese la nota del Taller 1 (entre 1 y 5): "))
nota_taller2 = float(input("Ingrese la nota del Taller 2 (entre 1 y 5): "))
nota_cuestionario1 = float(input("Ingrese la nota del Cuestionario 1 (entre 1 y 5): "))
nota_cuestionario2 = float(input("Ingrese la nota del Cuestionario 2 (entre 1 y 5): "))
nota_proyecto_final = float(input("Ingrese la nota del Proyecto Final (entre 1 y 5): "))

porcentaje_taller1 = 20 / 100
porcentaje_taller2 = 15 / 100
porcentaje_cuestionario1 = 22 / 100
porcentaje_cuestionario2 = 10 / 100
porcentaje_proyecto_final = 33 / 100

promedio_ponderado = (nota_taller1 * porcentaje_taller1) + (nota_taller2 * porcentaje_taller2) + (nota_cuestionario1 * porcentaje_cuestionario1) + (nota_cuestionario2 * porcentaje_cuestionario2) + (nota_proyecto_final * porcentaje_proyecto_final)

print(f"El promedio ponderado es: {promedio_ponderado}")
