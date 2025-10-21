"""
Este script define una lista de nombres y utiliza un bucle 'for'
junto con la sentencia 'continue' para mostrar en pantalla solo
aquellos nombres que no empiezan por la letra 'A' (ni mayúscula
ni minúscula).
"""
lista = ["Ana", "Luis", "Carlos", "Alberto", "Marta", "Sofía"]
for nombre in lista:
    if nombre.startswith('A') or nombre.startswith('a'):
        continue
    print(nombre)