from colas import ColaDeque


class ColaImpresion:
    def __init__(self):
        self.cola = ColaDeque()

    def agregar_trabajo(self, nombre_trabajo):
        self.cola.encolar(nombre_trabajo)
        print(f"Trabajo '{nombre_trabajo}' agregado a la cola.")

    def procesar_trabajo(self):
        if self.cola.esta_vacia():
            print("No hay trabajos en la cola.")
            return
        trabajo = self.cola.desencolar()
        print(f"Procesando trabajo '{trabajo}'.")

    def numero_de_trabajos(self):
        if not self.cola:
            print("La cola de impresión está vacía.")
            return
        print("Trabajos en la cola:",self.cola.tamano())

# Ejemplo de uso
cola_impresion = ColaImpresion()
cola_impresion.agregar_trabajo("Documento1.pdf")
cola_impresion.agregar_trabajo("Foto2.jpg")
cola_impresion.numero_de_trabajos()
cola_impresion.procesar_trabajo()
cola_impresion.procesar_trabajo()
cola_impresion.procesar_trabajo()