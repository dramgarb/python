productos = ["Pan", "Leche", "Huevos"]
precios = [1.20, 0.90, 2.50]

for prod, prec in zip(productos, precios):
    print(f"El producto {prod} vale {prec} euros")