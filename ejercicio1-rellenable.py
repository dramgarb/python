numeros = [10, 15, 20, 25, 30]
contador_pares = 0

# 1. Iniciamos el bucle para recorrer la lista 'numeros'
for n in numeros:
    # 2. Comprobamos si el número 'n' es par (resto igual a 0)
    if n % 2 == 0:
        # 3. Sumamos 1 al contador
        contador_pares += 1

print(f"Hay {contador_pares} números pares")
