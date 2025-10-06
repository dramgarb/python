edad = input("¿Cuál es tu edad? ")
if int(edad) < 18:
    print("Eres menor de edad")
elif int(edad) >= 18 and int(edad) < 65:
    print ("Eres adulto")
else:
    print("Eres adulto mayor")
