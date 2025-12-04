clase = [
    {"nombre": "Ana", "notas": [9, 8, 9, 7]},
    {"nombre": "Beto", "notas": [4, 3, 5, 2]},
    {"nombre": "Carla", "notas": [5, 6, 5, 5]},
    {"nombre": "Daniel", "notas": [9, 10, 10, 9]}
]
total_aprobados = 0
for alumno in clase:
    nota_media = sum(alumno["notas"]) / len(alumno["notas"])
    print(f"{alumno['nombre']} tiene una media de {nota_media}")
    if nota_media >= 5:
        total_aprobados += 1
print(f"En total an aprovado {total_aprobados} alumnos")