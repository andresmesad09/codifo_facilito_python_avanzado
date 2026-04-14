from collections import deque


class PilaDeque:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def agregar(self, item):
        self.items.append(item)

    def eliminar(self):
        if not self.esta_vacia():
            return self.items.pop()
        raise IndexError("Eliminar de una pila vacía")

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        raise IndexError("Pila vacía")

    def tamano(self):
        return len(self.items)

# Ejemplo de uso
pila_deque = PilaDeque()
pila_deque.agregar(1)
pila_deque.agregar(2)
print(pila_deque.eliminar())  # Salida: 2
print(pila_deque.cima())      # Salida: 1

