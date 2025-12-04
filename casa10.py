temperaturas = [12, -5, 0, -2, 8, -1, 10]
contador = 0
for temperaturas in temperaturas:
    if temperaturas < 0:
        contador += 1
print(f"Días con temperatura bajo cero {contador}")