from colas import ColaDeque


class ColaServicioCliente:
    def __init__(self):
        self.cola = ColaDeque()

    def agregar_cliente(self, nombre_cliente):
        self.cola.encolar(nombre_cliente)
        print(f"Cliente '{nombre_cliente}' agregado a la cola.")

    def atender_cliente(self):
        if self.cola.esta_vacia():
            print("No hay clientes en la cola.")
            return
        cliente = self.cola.desencolar()
        print(f"Atendiendo al cliente '{cliente}'.")

    def clientes_en_espera(self):
        print(f"Clientes en espera: {self.cola.tamano()}")

# Ejemplo de uso
cola_servicio_cliente = ColaServicioCliente()
cola_servicio_cliente.agregar_cliente("Angie")
cola_servicio_cliente.agregar_cliente("Mary")
cola_servicio_cliente.clientes_en_espera()  
cola_servicio_cliente.atender_cliente()
cola_servicio_cliente.agregar_cliente("Carina")
cola_servicio_cliente.atender_cliente()
cola_servicio_cliente.clientes_en_espera()