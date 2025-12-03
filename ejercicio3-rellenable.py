colores = ["Rojo", "Verde", "Azul"]

# 1. Convertir la lista en un iterador
mi_iterador = iter(colores)

# 2. Sacar el primer color
color1 = next(mi_iterador)
print(color1)

# 3. Sacar el segundo color
color2 = next(mi_iterador)
print(color2)
