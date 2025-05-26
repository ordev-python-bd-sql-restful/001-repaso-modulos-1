from .movimiento import MovimientoProducto

class Producto:
    def __init__(self, sku, nombre, descripcion, precio, cantidad):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio 
        self.cantidad = cantidad
        #movimientos en almacen
        self.movimientos = []

    def agregarMovimiento(self, movimiento: MovimientoProducto):
        self.movimientos.append(movimiento)

        #ajuste de inventario
        # si el movimiento es de entrada sumo 
        # si el movimiento es de salida resto a la cantidad en almacén
        if movimiento.tipo == "E":
            self.cantidad += movimiento.cantidad
        else:
            self.cantidad -= movimiento.cantidad

# Programa principal
if __name__ == "__main__":
    print("prueba" )