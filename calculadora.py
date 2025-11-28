def sumar(a, b):
    return (numero1 + numero2)


def restar(a, b):
    return (numero1 - numero2)


def multiplicar(a, b):
    return (numero1 * numero2)


def dividir(a, b):
    return (numero1 / numero2)


numero1 = float(input("Elige un numero "))
numero2 = float(input("Elige otro numero "))
print(f"El resultado de la suma es : ", sumar(numero1, numero2))
print(f"El resultado de la resta es: ", restar(numero1, numero2))
print(f"El resultado de la multiplicacion es: ", multiplicar(numero1, numero2))
print(f"El resultado de la division es: ", dividir(numero1, numero2))
