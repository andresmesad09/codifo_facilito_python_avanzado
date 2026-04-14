from collections import deque

# Implementación de cola usando deque
class ColaDeque:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        raise IndexError("Desencolar de una cola vacía")

    def frente(self):
        if not self.esta_vacia():
            return self.items[0]
        raise IndexError("Cola vacía")

    def tamano(self):
        return len(self.items)

# Ejemplo de uso
cola_deque = ColaDeque()
cola_deque.encolar(1)
cola_deque.encolar(2)
print(cola_deque.desencolar())  # Salida: 1
print(cola_deque.frente())      # Salida: 2
