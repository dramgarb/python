def mostrar_notas():
    """
    Lee el archivo de notas y las muestra numeradas en pantalla.
    Maneja errores si el archivo no existe o no se tienen permisos.
    """
    archivo = "notas.txt"
    modo = "r"
    encoding = "utf-8"

    try:
        with open(archivo, modo, encoding=encoding) as f:
            # Usamos readlines() para obtener una lista de líneas
            lineas = f.readlines()

            if not lineas:
                print("La lista de notas está vacía.")
            else:
                print("\nNotas actuales:")
                # Usamos enumerate empezando en 1, tal como vimos en la Unidad 2.10
                for i, nota in enumerate(lineas, start=1):
                    # .strip() elimina el salto de línea al mostrarlo
                    print(f"{i}. {nota.strip()}")

    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except PermissionError:
        print("Error: No tienes permisos para leer el archivo.")


def anadir_nota():
    """
    Pide un texto al usuario y lo añade al final del archivo.
    """
    texto = input("Escribe la nueva nota: ")
    archivo = "notas.txt"
    modo = "a"  # Modo 'append' para añadir al final sin borrar
    encoding = "utf-8"

    try:
        with open(archivo, modo, encoding=encoding) as f:
            f.write(f"{texto}\n")  # Añadimos salto de línea manual
        print("Nota guardada con éxito.")

    except PermissionError:
        print("Error: No tienes permisos para escribir en el archivo.")


def eliminar_nota():
    """
    Lee todas las notas, pide al usuario cuál borrar por su número,
    actualiza la lista y sobrescribe el archivo completo.
    """
    archivo = "notas.txt"
    modo_lectura = "r"
    modo_escritura = "w"
    encoding = "utf-8"

    try:
        # 1. Leemos todas las notas actuales
        lineas = []
        with open(archivo, modo_lectura, encoding=encoding) as f:
            lineas = f.readlines()

        if not lineas:
            print("No hay notas para eliminar.")
            return

        # Mostramos las notas para que el usuario sepa cuál elegir
        mostrar_notas()

        # 2. Pedimos el índice a eliminar
        entrada = input("\nNúmero de nota a eliminar: ")

        # Validación básica de número entero
        if not entrada.isdigit():
            print("Error: Debes introducir un número entero.")
            return

        indice = int(entrada) - 1  # Restamos 1 porque las listas empiezan en 0

        # 3. Validamos si el índice existe en la lista
        if 0 <= indice < len(lineas):
            # Usamos pop() como vimos en la Unidad 2.5 para sacar el elemento
            eliminada = lineas.pop(indice)

            # 4. Sobrescribimos el archivo con la lista actualizada
            with open(archivo, modo_escritura, encoding=encoding) as f:
                for linea in lineas:
                    f.write(linea)

            print(f"Nota eliminada correctamente: {eliminada.strip()}")
        else:
            print("Error: El número de nota no existe.")

    except FileNotFoundError:
        print("Error: El archivo de notas no se encuentra.")
    except PermissionError:
        print("Error: Permiso denegado.")


def main():
    """
    Función principal que gestiona el menú y el inicio del programa.
    """
    archivo = "notas.txt"

    print("📓 Gestor de Notas")

    # Lógica de inicio: Comprobar si existe, si no, crearlo.
    try:
        modo = "r"
        with open(archivo, modo, encoding="utf-8") as f:
            print(f"Archivo encontrado: {archivo}")
            mostrar_notas()
    except FileNotFoundError:
        print(f"Archivo {archivo} no encontrado. Creando uno nuevo...")
        modo = "w"
        with open(archivo, modo, encoding="utf-8") as f:
            pass  # Solo lo abrimos y cerramos para crearlo vacío

    # Bucle del menú principal
    opcion = ""
    while opcion != "4":
        print("\n--- Menú ---")
        print("1. Ver notas")
        print("2. Añadir nota")
        print("3. Eliminar nota")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        # Usamos match-case (Unidad 1.4)
        match opcion:
            case "1":
                mostrar_notas()
            case "2":
                anadir_nota()
            case "3":
                eliminar_nota()
            case "4":
                print("\n¡Hasta la próxima!")
            case _:
                print("Opción no reconocida. Inténtalo de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
