"""
b1_9_analizador_notas.py

Propósito: Calcular el promedio de tres notas ingresadas por el usuario.

El script incluye un error lógico intencional en la línea del cálculo
del 'promedio_erroneo'.

Error lógico:
El cálculo inicial se realizó como 'nota1 + nota2 + nota3 / 3'.
Esto es incorrecto porque la precedencia de operadores hace que solo
la 'nota3' se divida por 3. [cite: 181]

Corrección:
Para calcular el promedio correctamente, la suma debe ir entre paréntesis
para forzar que se ejecute primero: '(nota1 + nota2 + nota3) / 3'. [cite: 181]
"""

# Pedir la primera nota al usuario.
# Se usa float() para asegurar el tipo de dato correcto para operaciones matemáticas.
nota1 = float(input("Introduce la nota 1: "))

# Pedir la segunda nota al usuario.
nota2 = float(input("Introduce la nota 2: "))

# Pedir la tercera nota al usuario.
nota3 = float(input("Introduce la nota 3: "))

# CÁLCULO CON ERROR LÓGICO INTENCIONAL
# Este cálculo NO da el promedio correcto si las notas son diferentes. [cite: 169, 170]
promedio_erroneo = nota1 + nota2 + nota3 / 3

# Mostrar el resultado erróneo para que el depurador lo identifique.
print(f"El promedio calculado erróneamente es: {promedio_erroneo}")

# CÁLCULO CORREGIDO
# Esta es la fórmula correcta para el promedio. [cite: 181]
promedio_real = (nota1 + nota2 + nota3) / 3

# Mostrar el resultado real (para comparación post-depuración).
print(f"El promedio real es: {promedio_real}")