def recorrer_iterador() -> None:
    """Recorre un iterador usando next() con valor por defecto y muestra
los elementos.."""
    valores = [10, 20, 30, 40]
    it = iter(valores)
    elemento = next(it, None)
    while elemento is not None:
        print(f"Valor: {elemento}")


recorrer_iterador()
