def gestionar_alumno() -> None:
    """Gestiona y muestra información de un diccionario alumno."""
    alumno = {"nombre": "Pepe", "nota": 7, "curso": "asir"}
    for dato in alumno:
        print(f"{dato}: {alumno[dato]}")
    alumno["aprobado"] = True
    del alumno["curso"]
    for dato in alumno:
        print(f"{dato}: {alumno[dato]}.")


gestionar_alumno()
