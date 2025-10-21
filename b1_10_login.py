"""
Este script simula un sistema de login y registro para UN SOLO USUARIO
usando variables y estructuras de control básicas (if/else, while, for).
Implementa validaciones de seguridad para el identificador (email) y la
contraseña, y un límite de 3 intentos de inicio de sesión.
"""

# Variables globales para almacenar el UNICO usuario registrado.
usuario_registrado = ""
contrasena_registrada = ""

# Variable de control del bucle principal.
ejecutando = True

# FUNCIONES DE VALIDACIÓN

def validar_identificador(identificador):
    """Verifica si el identificador (email) cumple las reglas."""
    # REGLA 1: Mínimo 3 caracteres.
    if len(identificador) < 3:
        print("Error: El identificador debe tener al menos 3 caracteres.")
        return False

    # REGLA 2: Contener al menos '@'.
    if "@" not in identificador:
        print("Error: El identificador debe contener el símbolo '@'.")
        return False

    # REGLA 3: Contener al menos una de las extensiones.
    if not (".com" in identificador or ".es" in identificador or ".net" in identificador):
        print("Error: El identificador debe terminar en .com, .es, o .net.")
        return False

    # REGLA 4: No debe contener símbolos especiales (simplificado para principiantes).
    # Se asume que si cumple las reglas de email básico es suficiente a este nivel.

    return True

def validar_contrasena(contrasena):
    """Verifica si la contraseña cumple las reglas de seguridad."""
    # Variables de control para las reglas internas.
    tiene_mayuscula = False
    tiene_numero = False
    tiene_simbolo = False
    simbolos_validos = "!@#$%&*?"

    # REGLA 1: Mínimo 8 caracteres.
    if len(contrasena) < 8:
        print("Contraseña insegura. Debe tener al menos 8 caracteres.")
        return False

    # Bucle for para verificar mayúscula, número y símbolo.
    for caracter in contrasena:
        if 'A' <= caracter <= 'Z':  # Comprueba si es mayúscula.
            tiene_mayuscula = True
        if '0' <= caracter <= '9':  # Comprueba si es un número.
            tiene_numero = True
        if caracter in simbolos_validos: # Comprueba si es uno de los símbolos especiales.
            tiene_simbolo = True

    # REGLA 2: Contener al menos una mayúscula.
    if not tiene_mayuscula:
        print("Contraseña insegura. Debe contener al menos una mayúscula.")
        return False

    # REGLA 3: Contener al menos un número.
    if not tiene_numero:
        print("Contraseña insegura. Debe contener al menos un número.")
        return False

    # REGLA 4: Contener al menos un símbolo especial.
    if not tiene_simbolo:
        print("Contraseña insegura. Debe contener al menos un símbolo (!@#$%&*?).")
        return False

    return True

# LÓGICA DEL PROGRAMA PRINCIPAL (Bucle While)

# Bucle principal para mantener el menú activo.
while ejecutando:
    print("\n-------------------------------------------")
    print("¿Qué quieres hacer? [1] Registrarse  [2] Iniciar sesión  [3] Salir")
    opcion = input("Elige una opción: ")

    # Opción 1: REGISTRARSE
    if opcion == '1':
        print("\n--- REGISTRO ---")

        # Bucle para validar y pedir el identificador hasta que sea correcto.
        while True:
            nuevo_usuario = input("Introduce un nombre de usuario (email): ")
            if validar_identificador(nuevo_usuario):
                break

                # Bucle para validar y pedir la contraseña hasta que sea correcta.
        while True:
            nueva_contrasena = input("Introduce una contraseña: ")
            if validar_contrasena(nueva_contrasena):
                break

        # Almacenar el usuario y la contraseña.
        usuario_registrado = nuevo_usuario
        contrasena_registrada = nueva_contrasena
        print("Usuario registrado con éxito.")

    # Opción 2: INICIAR SESIÓN
    elif opcion == '2':
        print("\n--- INICIO DE SESIÓN ---")

        # Verificar si hay datos registrados.
        if usuario_registrado == "":
            print("No hay usuarios registrados. Por favor, regístrate primero.")
            continue

        # Solicitar el identificador para iniciar sesión.
        login_usuario = input("Introduce tu usuario: ")

        # Comprobar si el identificador coincide.
        if login_usuario == usuario_registrado:
            intentos = 0
            MAX_INTENTOS = 3

            # Bucle while para controlar los 3 intentos de contraseña.
            while intentos < MAX_INTENTOS:
                login_contrasena = input("Introduce tu contraseña: ")

                # Comprobar si la contraseña es correcta.
                if login_contrasena == contrasena_registrada:
                    print(f"Acceso concedido. Bienvenida, {usuario_registrado}.")
                    break # Salida del bucle de intentos (sesión exitosa).
                else:
                    intentos += 1
                    if intentos < MAX_INTENTOS:
                        print(f"Acceso denegado. Intento {intentos}/{MAX_INTENTOS}")

            # Si se sale del bucle 'while' porque 'intentos' alcanzó el máximo.
            if intentos == MAX_INTENTOS:
                print("Demasiados intentos fallidos. Regresando al menú principal.")

        else:
            print("Acceso denegado. Usuario no encontrado.")


    # Opción 3: SALIR
    elif opcion == '3':
        print("Saliendo del programa. Hasta pronto!")
        ejecutando = False # Finaliza el bucle 'while'.

    # Opción Inválida
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")