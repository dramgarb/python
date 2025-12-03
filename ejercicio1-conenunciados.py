# 1. Crea una lista llamada 'notas' con estos valores: 4, 6, 8, 3, 5
notas = [4, 6, 8, 3, 5]

# 2. Crea una variable 'contador' y ponla a cero
contador = 0

# 3. Haz un bucle for que recorra cada 'nota' en la lista 'notas'
for notas in notas:

    # 4. Dentro del bucle: Si la 'nota' es mayor o igual a 5
    if notas >= 5:
        # 5. Suma 1 al contador
        contador += 1

    # 6. Fuera del bucle, imprime el resultado final con un f-string
print(f"Contador: {contador}")
