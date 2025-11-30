"""Listas"""
estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

"""Bucle usando enumerate y zip"""
for indice, (nombre, mat, fis, quim) in enumerate(zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica), start=1):

    """Pormedio"""
    promedio = (mat + fis + quim) / 3

    """Calificacion final"""
    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    else:
        estado = "Reprobado"

    """Lo imprimimos"""
    print(f"{indice} {nombre} - Matemáticas: {mat}, Física: {fis}, Química: {quim}, Promedio: {promedio:.2f}, Estado: {estado}")