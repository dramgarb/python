productos = [
    {"nombre": "Camiseta", "precio": 15, "stock": 10},
    {"nombre": "Pantalón", "precio": 30, "stock": 2},
    {"nombre": "Zapatos", "precio": 50, "stock": 4},
    {"nombre": "Gorra", "precio": 10, "stock": 20}
]

for articulo in productos:
    if articulo["stock"] < 5:
        print(f"Urgente reponer: {articulo["nombre"]}")

valor_total = 0
for prec in productos:
    valor_total += prec["precio"] * prec["stock"]
print(f"El precio total gastado a sido: {valor_total}")