class MovimientoProducto:
    def __init__(self, fecha, tipo, cantidad, producto = None):
        self.fecha = fecha
        self.tipo = tipo 
        self.cantidad = cantidad
        self.producto = producto