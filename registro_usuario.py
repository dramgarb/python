"""Esta funcion registra un usuario con su nombre, edad y ciudad."""


def registrar_usuario(nombre, edad, ciudad="Madrid"):
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")


# Esta llamada serviria para la posicional y para la de valor por defecto
registrar_usuario("Ana", 20)
# Y esta seria para llamarla nombrando los parametros para poder ponerlos desordenados
registrar_usuario(edad=25, ciudad="Huelva", nombre="Luis")
