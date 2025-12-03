alumnos = ["Luis", "Marta", "Pepe", "Sara"]
notas = [4, 8, 3, 9]

alumnos_aprobados = 0
alumnos_suspensos = 0

for alumnos, notas in zip(alumnos, notas):
    if notas >= 5:
        alumnos_aprobados += 1
    elif notas < 5:
        alumnos_suspensos += 1
    else:
        print("nota no valida")

print(f"aprobados:  {alumnos_aprobados}, suspensos: {alumnos_suspensos}")
