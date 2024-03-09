
notas = {
    'Taller 1': 4,
    'Taller 2': 5,
    'Cuestionario 1': 3,
    'Cuestionario 2': 4,
    'Proyecto final': 5
}

porcentajes = {
    'Taller 1': 20,
    'Taller 2': 15,
    'Cuestionario 1': 22,
    'Cuestionario 2': 10,
    'Proyecto final': 33
}


promedio_ponderado = sum(notas[curso] * (porcentaje / 100) for curso, porcentaje in porcentajes.items())

print(f"El promedio ponderado es: {promedio_ponderado}")
