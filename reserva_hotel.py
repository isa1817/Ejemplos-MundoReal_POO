class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} (C.I. {self.cedula})"

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False
        self.cliente = None

    def reservar(self, cliente):
        if not self.ocupada:
            self.ocupada = True
            self.cliente = cliente
            print(f"Habitación {self.numero} reservada por {cliente}.")
        else:
            print(f"Habitación {self.numero} ya está ocupada.")

    def liberar(self):
        if self.ocupada:
            print(f"Habitación {self.numero} liberada.")
            self.ocupada = False
            self.cliente = None
        else:
            print(f"Habitación {self.numero} ya está libre.")

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_disponibles(self):
        print(f"Habitaciones disponibles en el hotel {self.nombre}:")
        for h in self.habitaciones:
            if not h.ocupada:
                print(f" - Habitación {h.numero} ({h.tipo}) - ${h.precio}")

if __name__ == "__main__":
    hotel = Hotel("Amazon Lodge")
    h1 = Habitacion(101, "Simple", 35)
    h2 = Habitacion(102, "Doble", 50)
    hotel.agregar_habitacion(h1)
    hotel.agregar_habitacion(h2)
    hotel.mostrar_disponibles()

    cliente1 = Cliente("Ana Pérez", "1002003000")
    h1.reservar(cliente1)
    hotel.mostrar_disponibles()
    h1.liberar()
    hotel.mostrar_disponibles()
