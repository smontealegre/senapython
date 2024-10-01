def imprima_producto(nombre, precio):
    print(f"Producto: {nombre} - Precio: ${precio}")

def caja():
    total = 0  # Inicializar la variable total

    while True:
        nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        
        if nombre.lower() == 'fin':
            break  # Salir del bucle si el usuario ingresa 'fin'

        try:
            precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("¡Error! Ingrese un valor numérico para el precio.")
            continue  # Volver al inicio del bucle si hay un error

        imprima_producto(nombre, precio)
        total += precio  # Sumar el precio al total

    print("\nTotal a pagar: $", total)

# Llamar a la función caja para probar el programa
caja()
