from sortedcontainers import SortedList

lista = SortedList([5, 3, 7, 2, 4, 6, 8])
print(lista)  # Salida: SortedList([2, 3, 4, 5, 6, 7, 8])
print(5 in lista)
lista.add(12)
print(lista.index(12))