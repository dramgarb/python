def crear_perfil(nombre, email, edad=18):
    return {"nombre": nombre, "email": email, "edad": edad}


usuario = crear_perfil("carlos", "carlos@asd.com")
print("inicial: ", usuario)

usuario["telefono"] = 111222333

email_borrado = usuario.pop("email")
print(f"email eliminado: {email_borrado}")
print("final: ", usuario)
