"""listas"""

estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

"""diccionario"""

resultado_final = {}


"""recorrer listas al mismo tiempo"""
for nombre, n_mat, n_fis, n_quim in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):

    """Calcular promedio"""

    promedio = (n_mat + n_fis + n_quim) / 3

    """Estado"""

    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperacion"
    else:
        estado = "Reprobado"

    """Guardar la informacion"""

    resultado_final[nombre] = {
        "Matematicas": n_mat,
        "Fisica": n_fis,
        "Quimica": n_quim,
        "Promedio": round(promedio, 2),
        "Estado": estado
    }
"""imprimir resultado"""

for nombre, info in resultado_final.items():
    print(f"{nombre} - Matematicas: {info['Matematicas']}, "
          f"Fisica: {info['Fisica']}, "
          f"Quimica: {info['Quimica']}, "
          f"Promedio: {info['Promedio']}, "
          f"Estado: {info['Estado']}"
          )
