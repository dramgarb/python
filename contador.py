contador = 0

"""Con global llamo a la variable contador y le sumo uno"""


def incrementar():
    global contador
    contador += 1


"""Con global llamo a la variable contador y le resto uno"""


def decrementar():
    global contador
    contador -= 1


"""muestra contador"""


def mostrar_contador():
    print(contador)


incrementar()
incrementar()
decrementar()
mostrar_contador()
