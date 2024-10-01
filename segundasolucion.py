def registrar_venta(*args, **kwargs):
    venta = {"paquete": args[0] if args else None,
             "vendedor": args[1] if len(args) > 1 else None,
             "precio_venta": kwargs.get("precio_venta", None)}
    return venta

def calcular_monto_total_ventas(ventas):
    total_ventas = sum(venta["precio_venta"] for venta in ventas if "precio_venta" in venta)
    return total_ventas

def calcular_comision(vendedor, ventas, porcentaje_comision):
    comision_vendedor = sum(venta["precio_venta"] * porcentaje_comision / 100
                            for venta in ventas
                            if "vendedor" in venta and venta["vendedor"] == vendedor)
    return comision_vendedor

def generar_informe_ventas(ventas):
    print("Informe de Ventas:")
    for venta in ventas:
        paquete = venta.get("paquete", "No especificado")
        vendedor = venta.get("vendedor", "No especificado")
        precio_venta = venta.get("precio_venta", "No especificado")
        print(f"Paquete: {paquete}, Vendedor: {vendedor}, Precio de Venta: {precio_venta}")
"""
 Programa principal (While, métodos de tupla 'append' predispuestos con el efecto de insertar elementos, imprime los resultados de los informes pedidos
 por el usuario)
"""
ventas = []

while True:
    paquete = input("Ingrese el nombre del paquete (o 'fin' para terminar): ")
    if paquete.lower() == 'fin':
        break

    vendedor = input("Ingrese el nombre del vendedor: ")
    precio_venta = float(input("Ingrese el precio de venta: "))

    venta_actual = registrar_venta(paquete, vendedor=vendedor, precio_venta=precio_venta)
    ventas.append(venta_actual)

print("\nResumen de Ventas:")
generar_informe_ventas(ventas)

total_ventas = calcular_monto_total_ventas(ventas)
print(f"\nMonto total de ventas: {total_ventas}")

vendedor_comision = input("Ingrese el nombre del vendedor para calcular la comisión: ")
porcentaje_comision = float(input("Ingrese el porcentaje de comisión: "))
comision_total = calcular_comision(vendedor_comision, ventas, porcentaje_comision)
print(f"\nComisión total para {vendedor_comision}: {comision_total}")
