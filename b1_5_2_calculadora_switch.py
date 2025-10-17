num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación suma, resta, multiplicación o división: ")
match operacion:
    case "suma":
        print(num1 + num2)
    case "resta":
        print(num1 - num2)
    case "multiplicación":
        print(num1 * num2)
    case "división":
        print(num1 / num2)
    case _:
        print("Operación no reconocida")