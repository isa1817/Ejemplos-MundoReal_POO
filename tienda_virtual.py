class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)
        print(f"Producto agregado: {producto}")

    def total(self):
        return sum([p.precio for p in self.productos])

    def mostrar(self):
        print("Productos en el carrito:")
        for p in self.productos:
            print(f" - {p}")

if __name__ == "__main__":
    p1 = Producto("Camisa", 15)
    p2 = Producto("Pantalón", 25)
    carrito = Carrito()
    carrito.agregar(p1)
    carrito.agregar(p2)
    carrito.mostrar()
    print(f"Total a pagar: ${carrito.total()}")
