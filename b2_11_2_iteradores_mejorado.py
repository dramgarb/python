estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}

"""Creación del iterador sobre las claves del diccionario"""
iterador_nombres = iter(estudiantes)

while True:
    """Extraemos el siguiente nombre. Si no quedan elementos, devuelve None."""
    nombre = next(iterador_nombres, None)

    """Control de salida: si es None, terminamos la iteración"""
    if nombre is None:
        break

    """Procesamiento"""
    notas = estudiantes[nombre]
    promedio = sum(notas) / len(notas)

    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    else:
        estado = "Reprobado"

    print(f"{nombre} - Notas: {notas}, Promedio: {promedio:.2f}, Estado: {estado}")