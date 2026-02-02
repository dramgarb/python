def recorrer_iterador() -> None:
    """Recorre un iterador sobre las claves de un diccionario usando next() con valor por
   defecto."""


edades = {"Ana": 20, "Luis": 22, "Marta": 21}
it = iter(edades)
nombre = next(it, None)
while nombre is not None:
    print(f"Nombre: {nombre}, Edad:  {edades[nombre]}.")
    nombre = next(it, None)
recorrer_iterador()
