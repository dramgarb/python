numeros = [10, 20, 30, 40]
iterador2 = iter(numeros)
elemento = next(iterador2, None)

while elemento is not None:
    print(f"Procesando: {elemento}")
    elemento = next(iterador2, None)
