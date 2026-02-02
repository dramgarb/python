def contar_numeros(valor: int) -> None:
    """Cuenta cuántas veces aparece un número en una lista interna y muestra el
   resultado."""


numeros = [5, 3, 5, 2, 5, 7, 3]
contador_numero = 0
for numero in numeros:
    if numero == 5:
        contador_numero += 1
        print(f"El numero {numero} aparece {contador_numero} veces")
    else:
        print(f"El numero {numero} no aparece")
contar_numeros(5)
contar_numeros(3)
contar_numeros(8)
