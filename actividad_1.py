def contar_apariciones(nombre_elemento: str) -> None:
    """Busca cuántas veces aparece un elemento en la lista interna y
muestra el resultado.."""
    elementos = ["python", "java", "python", "c", "python", "go",
                 "java"]
    n = len(nombre_elemento)
    if n >= 1:
        print(f"El elemento {nombre_elemento} aparece {n} veces")
    else:
        print(f"El elemento {nombre_elemento} no esta en la lista")


contar_apariciones("python")
contar_apariciones("java")
contar_apariciones("ruby")
