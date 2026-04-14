from pilas import PilaDeque


class Navegador:
    def __init__(self):
        self.historial_atras = PilaDeque()
        self.historial_adelante = PilaDeque()
        self.pagina_actual = None

    def visitar(self, pagina):
        if self.pagina_actual is not None:
            self.historial_atras.agregar(self.pagina_actual)
        self.pagina_actual = pagina
        # Limpiar el historial de adelante al visitar una nueva página
        self.historial_adelante = PilaDeque()

    def atras(self):
        if self.historial_atras.esta_vacia():
            print("No hay páginas para ir hacia atrás.")
            return
        self.historial_adelante.agregar(self.pagina_actual)
        self.pagina_actual = self.historial_atras.eliminar()

    def adelante(self):
        if self.historial_adelante.esta_vacia():
            print("No hay páginas para ir hacia adelante.")
            return
        self.historial_atras.agregar(self.pagina_actual)
        self.pagina_actual = self.historial_adelante.eliminar()

    def pagina_actual(self):
        return self.pagina_actual if self.pagina_actual is not None else "Ninguna página visitada"

# Ejemplo de uso
navegador = Navegador()
navegador.visitar("pagina1.com")
print(navegador.pagina_actual)  # Debería imprimir "pagina1.com"

navegador.visitar("pagina2.com")
print(navegador.pagina_actual)  # Debería imprimir "pagina2.com"

navegador.atras()
print(navegador.pagina_actual)  # Debería imprimir "pagina1.com"

navegador.adelante()
print(navegador.pagina_actual)  # Debería imprimir "pagina2.com"

navegador.atras()
navegador.atras()  # Debería imprimir "No hay páginas para ir hacia atrás."