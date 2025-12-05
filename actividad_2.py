def gestionar_persona() -> None:
    """Realiza exactamente los pasos indicados sobre el diccionario
persona."""
    persona = {"nombre": "Ana", "edad": "30", "ciudad": "Madrid"}
    for datos in persona:
        print("nombre:", persona.get("nombre"))
        print("edad:", persona.get("edad"))
        print("ciudad:", persona.get("ciudad"))
        break
    persona["profesion:"] = "Ingeniera"
    del persona["ciudad"]
    for datos in persona:
        print(persona)
        break


gestionar_persona()
