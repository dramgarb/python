# Actividad de contar sin datos por teclado


temperaturas = [12, -2, 0, 5, -8, 20, -1, 15]
contador_frio = 0
contador_calor = 0

for temp in temperaturas:
    if temp < 0:
        contador_frio += 1
    else:
        contador_calor += 1

print(f"dias frios: {contador_frio}")
print(f"dias calurosos: {contador_calor}")
