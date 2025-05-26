from .producto import Producto
from .movimiento import MovimientoProducto

def leer_movimiento():
    t = input("Tipo de Movimiento: ").upper()
    c = int(input("Cantidad: "))
    f = input("Fecha (d/M/A): ")
    return  MovimientoProducto(f,t,c)

def imprimir_producto(p: Producto):
    print(f"SKU {p.sku}")
    print(f"Nombre {p.nombre}")
    print(f"Cantidad: {p.cantidad}")
    print("Movimientos: ")
    for m in p.movimientos:
        print(f"- Fecha: {m.fecha}, Tipo: {m.tipo}, Cantidad: {m.cantidad}")
