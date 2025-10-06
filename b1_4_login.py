usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("¿Cuál es tu nombre de usuario? ")
contrasena = input("¿Cuál es tu contraseña? ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")