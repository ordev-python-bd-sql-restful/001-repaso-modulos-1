from ferreteria.producto import Producto
from ferreteria.movimiento import MovimientoProducto
from ferreteria import utils_inventario

p = Producto("P001", "producto prueba", "", "250", 3)

m = utils_inventario.leer_movimiento()
p.agregarMovimiento(m)

m = utils_inventario.leer_movimiento()
p.agregarMovimiento(m)

utils_inventario.imprimir_producto(p)