num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación suma, resta, multiplicación o división: ")
if operacion == "suma":
    print(num1 + num2)
elif operacion == "resta":
    print(num1 - num2)
elif operacion == "multiplicación":
    print(num1 * num2)
elif operacion == "división":
    print(num1 / num2)
else:
    print("Operación no reconocida")
