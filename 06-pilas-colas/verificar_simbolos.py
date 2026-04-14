from pilas import PilaDeque


def verificar_simbolos(cadena):
    pila = PilaDeque()
    pares = {')': '(', '}': '{', ']': '['}
    for char in cadena:
        if char in '({[':
            pila.agregar(char)
        elif char in ')}]':
            if pila.esta_vacia() or pila.eliminar() != pares[char]:
                return False
    return pila.esta_vacia()

print(verificar_simbolos("({[]})"))          # Debería devolver True
print(verificar_simbolos("({[)"))            # Debería devolver False
print(verificar_simbolos("{[()]}"))          # Debería devolver True
print(verificar_simbolos("(((()))"))         # Debería devolver False