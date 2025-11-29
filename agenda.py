from numbers import Number

agenda = {}
print(f"Escribe el nombre y el telefono de dos contactos")


"""Pedimos al usuario que añada los contactos"""


Nombre = input("Introcuce el Nombre del contacto: ")
Telefono = input("Introduce el telefono para el contacto: ")
agenda[Nombre] = Telefono
Nombre2 = input("Introduce el Nombre del segundo contacto: ")
Telefono2 = input("Introduce el Telefono del segundo contacto: ")
agenda[Nombre2] = Telefono2

"""Mostramos la agenda completa"""


for Nombre, Telefono in agenda.items():
    print(Nombre, ":", Telefono)


"""Buscar en el diccionario"""

buscar = input("Pon el nombre del contacto que buscas: ")
if buscar in agenda:
    print(f"El telefono que ese contacto es: ",Telefono)
else:
    print("No existe")
