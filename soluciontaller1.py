def obtener_edades():
    edades_pasajeros = []
    
    while len(edades_pasajeros) < 5:
        try:
            edad = int(input("Ingrese la edad del pasajero (número entero positivo): "))
            
            if edad < 0:
                print("Por favor, ingrese un número entero positivo.")
                continue

            edades_pasajeros.append(edad)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    return edades_pasajeros

def calcular_promedio(edades):
    if len(edades) == 0:
        return 0
    
    suma_edades = sum(edades)
    promedio = suma_edades / len(edades)
    return promedio

def principal():
    edades_pasajeros = obtener_edades()

    promedio = calcular_promedio(edades_pasajeros)

    print(f"El promedio de edades de los pasajeros es: {promedio:.2f}")

# Llamar a la función principal para ejecutar el programa
principal()
