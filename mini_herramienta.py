import math
import os

import requests  # Librería externa (requiere pip install requests)


def opcion_matematicas():
    """
    Pide un número y realiza cálculos usando el módulo math.
    Gestiona errores si el usuario no introduce un número válido.
    """
    print("\n--- Cálculos Matemáticos ---")
    try:
        entrada = input("Introduce un número entero positivo: ")
        numero = int(entrada)

        if numero < 0:
            print("Error: Para calcular el factorial y la raíz, el número debe ser positivo.")
        else:
            # Usamos funciones del módulo math (Unidad 3.2)
            raiz = math.sqrt(numero)
            factorial = math.factorial(numero)
            potencia = math.pow(numero, 2)

            print(f"Raíz cuadrada: {raiz}")
            print(f"Factorial: {factorial}")
            print(f"Potencia al cuadrado: {potencia}")

    except ValueError:
        print("Error: Debes introducir un número entero válido.")


def opcion_explorador():
    """
    Muestra el directorio actual, lista archivos y permite crear carpetas usando el módulo os.
    """
    print("\n--- Explorador de Directorios ---")

    # 1. Mostrar directorio actual (os.getcwd)
    ruta_actual = os.getcwd()
    print(f"Directorio actual: {ruta_actual}")

    # 2. Listar archivos (os.listdir)
    print("Archivos en la carpeta:")
    try:
        archivos = os.listdir(".")
        for archivo in archivos:
            print(f"- {archivo}")
    except OSError:
        print("Error al leer el directorio.")

    # 3. Crear carpeta nueva
    crear = input("\n¿Quieres crear una nueva carpeta? (s/n): ").lower()

    if crear == "s":
        nombre_carpeta = input("Introduce el nombre de la carpeta: ")
        try:
            # os.mkdir crea una carpeta
            os.mkdir(nombre_carpeta)
            print("Carpeta creada con éxito.")
        except FileExistsError:
            print("Error: La carpeta ya existe.")
        except PermissionError:
            print("Error: No tienes permisos para crear carpetas aquí.")


def opcion_api():
    """
    Realiza una petición HTTP a GitHub usando la librería externa requests.
    Maneja excepciones de conexión.
    """
    print("\n--- Consulta a API (requests) ---")
    url = "https://api.github.com"
    print(f"Petición a {url} ...")

    try:
        # Petición GET usando la librería externa
        respuesta = requests.get(url)

        # Mostramos los datos solicitados
        print(f"Código de estado: {respuesta.status_code}")

        texto_respuesta = respuesta.text
        longitud = len(texto_respuesta)
        print(f"Tamaño de la respuesta: {longitud} caracteres")

        print("Contenido (primeros 200 caracteres):")
        print(texto_respuesta[:200])

    except requests.exceptions.RequestException:
        # Capturamos cualquier error relacionado con la librería requests
        print("Error: No se pudo conectar a la API. Revisa tu conexión a internet.")


def main():
    """
    Función principal con el menú de opciones.
    """
    opcion = ""

    while opcion != "4":
        print("\n--- Menú de Herramientas ---")
        print("1. Cálculos matemáticos")
        print("2. Explorador de directorios")
        print("3. Consulta a API (requests)")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        # Control de flujo con match-case (Unidad 1.4)
        match opcion:
            case "1":
                opcion_matematicas()
            case "2":
                opcion_explorador()
            case "3":
                opcion_api()
            case "4":
                print("\n¡Hasta la próxima!")
            case _:
                print("Opción no válida. Por favor, elige entre 1 y 4.")


if __name__ == "__main__":
    main()
