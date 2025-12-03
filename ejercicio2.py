# Gestionar datos de una persona

persona = {"nombre": "ana", "edad": 25, "ciudad": "madrid"}


def actualizar_ciudad(datos_persona, nueva_ciudad):
    datos_persona["ciudad"] = nueva_ciudad
    print(f"Datos actualizados: {datos_persona}")


actualizar_ciudad(persona, "barcelona")
