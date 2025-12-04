corredores = ["Marta", "Pablo", "Lucía"]
tiempos = [12.5, 13.1, 13.4]

for i ,(nombre, tiempo) in enumerate(zip(corredores, tiempos), start=1):
    print(f"Llegada #1 {nombre} hizo {tiempo}s")