alumno = {"nombre": "Lucia", "curso": "2ºbachillerato", "notas": {"matematicas": 8, "historia": 6, "ingles": 9}}

historia = alumno["notas"]["historia"]
ingles = alumno["notas"]["ingles"]
resultado = (historia + ingles) / 2
print(f"La media de letras de Lucia es {resultado}")