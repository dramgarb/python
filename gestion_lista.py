compras = []

compras.append(input(f"Cual es el primer producto "))
compras.append(input(f"Cual es el segundo producto "))
compras.append(input("Cual es el tercer producto "))
compras.append(input("Cual es el cuarto producto "))
compras.append(input("Cual es el ultimo producto "))

print(compras)

compras.remove(input(f"Que producto quieres eliminar "))

compras.sort()
print(compras)
