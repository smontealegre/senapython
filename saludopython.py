def saludo():
    global nombre, apellido1, apellido2
    print(f"¡Hola!, mi nombre es {nombre} {apellido1} {apellido2}")

nombre = str(input("¿Cuál es tu nombre? "))
apellido1 = str(input("Tu apellido: "))
apellido2 = str(input("Y tu segundo apellido: "))

saludo()

