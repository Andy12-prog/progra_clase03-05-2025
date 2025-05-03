class Casa:
    def __init__(self, direccion, habitaciones, tiene_jardin):
        self.direccion = direccion
        self.habitaciones = habitaciones
        self.tiene_jardin = tiene_jardin

    def mostrar_informacion(self):
        jardin = "sí" if self.tiene_jardin else "no"
        print(f"Dirección: {self.direccion}")
        print(f"Número de habitaciones: {self.habitaciones}")
        print(f"Tiene jardín: {jardin}")

    def agregar_habitacion(self):
        self.habitaciones += 1
        print(f"Se ha añadido una habitación. Ahora hay {self.habitaciones} habitaciones.")

    def cambiar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"La dirección ha sido actualizada a: {self.direccion}")

mi_casa = Casa("Calle Falsa 123", 3, True)
mi_casa.mostrar_informacion()
mi_casa.agregar_habitacion()
mi_casa.cambiar_direccion("Avenida Siempreviva 742")
mi_casa.mostrar_informacion()
mi_casa.mostrar_habitacion2()
