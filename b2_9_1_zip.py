nombres = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]

for nombres, notas_matematicas, notas_fisica in zip(nombres, notas_matematicas, notas_fisica):
    print(nombres, "-" ,"Matematicas: ",notas_matematicas, "Fisica: ",notas_fisica)