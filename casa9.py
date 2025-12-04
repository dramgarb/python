cola = [
    {"nombre": "Ana", "edad": 17},
    {"nombre": "Beto", "edad": 25},
    {"nombre": "Carla", "edad": 15}
]

def verificar_acceso(persona):
    # CORRECCIÓN 1: Miramos directamente la edad de "persona"
    if persona["edad"] >= 18:
        print(f"Adelante {persona['nombre']}")
    else:
        print(f"{persona['nombre']}")

# CORRECCIÓN 2: Usamos un bucle para pasar a la gente de uno en uno
print("--- Control de Acceso ---")
for alguien in cola:
    verificar_acceso(alguien)