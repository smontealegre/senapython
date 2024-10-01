def registrar_venta(paquete, vendedor, precio_venta):
    venta = [paquete, vendedor, precio_venta]
    return venta

def calcular_monto_total_ventas(ventas):
    total_ventas = sum(venta[2] for venta in ventas)
    return total_ventas

def calcular_comision(vendedor, ventas, porcentaje_comision):
    comision_vendedor = sum(venta[2] * porcentaje_comision / 100 for venta in ventas if venta[1] == vendedor)
    return comision_vendedor

def generar_informe_ventas(ventas):
    print("Informe de Ventas:")
    for paquete, vendedor, precio_venta in ventas:
        print(f"Paquete: {paquete}, Vendedor: {vendedor}, Precio de Venta: ${precio_venta}")

# Programa principal
ventas = []

while True:
    paquete = input("Ingrese el nombre del paquete (o 'fin' para terminar): ")
    if paquete.lower() == 'fin':
        break

    vendedor = input("Ingrese el nombre del vendedor: ")
    precio_venta = float(input("Ingrese el precio de venta: "))

    venta_actual = registrar_venta(paquete, vendedor, precio_venta)
    ventas.append(venta_actual)