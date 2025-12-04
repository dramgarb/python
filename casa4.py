jugadores = ["Ana", "Beto", "Carla"]
puntos = [5000, 4500, 6000]

for i, (j, p) in enumerate(zip(jugadores, puntos), start=1):
    print(f"Ranking #{i} {j} tiene {p} puntos")