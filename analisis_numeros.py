"""lista de 20 numeros"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

"""dentro de cuadrados meto los numero al cuadrado que esten dentro de la lista"""
cuadrados = [numeros ** 2 for numeros in numeros]
"""dentro de pares meto los numero que % 2 sea = a 0"""
pares = [numeros % 2 == 0 for numeros in numeros]
"""dentro de mayor_10 meto los numero de la lista que sean mayores a 10"""
mayor_10 = [numeros > 10 for numeros in numeros]

"""aqui los imprimo pero no entiendo porque si en el primero me imprime los numero en los otros dos que los hago de la misma forma me pone
true y false"""
print(cuadrados)
print(pares)
print(mayor_10)