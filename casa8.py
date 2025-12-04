precios = [100, 50, 200, 80]

# 1. Definimos la "máquina" de calcular
def calcular_descuento(precio_original):
    nuevo_precio = precio_original * 0.8
    return nuevo_precio # ¿Qué variable devolvemos?

# 2. Programa principal
print("--- Rebajas ---")
for p in precios:
    # 3. Llamamos a la función
    precio_final = calcular_descuento(p)
    print(f"De {p}€ baja a {precio_final}€")