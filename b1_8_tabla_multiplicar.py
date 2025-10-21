"""
Solicitar al usuario dos números y una operación (suma, resta, multiplicación, división).
Realizar la operación indicada con los dos números y mostrar el resultado.
"""
# Solicitar al usuario dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
# Solicitar la operación
operacion = input("Ingrese la operación suma, resta, multiplicación o división: ")
# Realizar la operación indicada y mostrar el resultado
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
