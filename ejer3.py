class Factura:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, nombre, precio, cantidad):
        self.productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    
    def calcular_total(self):
        return sum(producto["precio"] * producto["cantidad"] for producto in self.productos)
    
    def mostrar_factura(self):
        print("Factura:")
        for producto in self.productos:
            print(f"{producto['nombre']}: ${producto['precio']} x {producto['cantidad']} = ${producto['precio'] * producto['cantidad']}")
        print(f"Total: ${self.calcular_total()}")

#ejem
factura1 = Factura()
factura1.agregar_producto("Play 5", 2900000, 1)
factura1.agregar_producto("Control Play 5", 80000, 2)
factura1.mostrar_factura()
