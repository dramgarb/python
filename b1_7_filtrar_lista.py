
lista = ["Ana", "Luis", "Carlos", "Alberto", "Marta", "Sofía"]
for nombre in lista:
    if nombre.startswith('A') or nombre.startswith('a'):
        continue
    print(nombre)