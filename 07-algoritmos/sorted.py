arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = sorted(arr) 
#sorted(iterable, key=None, reverse=False) usa el TIMSORT variable del MERGESORT y el QUICKSORT
print("Sorted array:", sorted_arr)


arr = [3, 6, 8, 10, 1, 2, 1]
arr.sort()
print("Sorted array:", arr)

"""
Diferencias entre estos dos métodos:
Modificación: .sort() modifica la lista original; sorted() devuelve una nueva lista.
Aplicación: .sort() solo se puede usar con listas; sorted() se puede usar con cualquier iterable.
Valor de Retorno: .sort() retorna None; sorted() retorna una nueva lista ordenada.
Uso: Ambos aceptan key y reverse para personalizar el ordenamiento
"""

diccionario = {
    'item1': {'campo1': 2, 'campo2': 3},
    'item2': {'campo1': 1, 'campo2': 4},
    'item3': {'campo1': 2, 'campo2': 1},
    'item4': {'campo1': 1, 'campo2': 2},
}

# Convertir el diccionario en una lista de tuplas (clave, valor)
items = list(diccionario.items())

print(items)

# Ordenar por 'campo1' primero y luego por 'campo2'
ordenado = sorted(items, key=lambda x: (x[1]['campo1'], x[1]['campo2']))

# Convertir la lista de nuevo en un diccionario
diccionario_ordenado = dict(ordenado)

print(diccionario_ordenado)
"""
RESULTADO
{
    'item2': {'campo1': 1, 'campo2': 2},
    'item4': {'campo1': 1, 'campo2': 4},
    'item3': {'campo1': 2, 'campo2': 1},
    'item1': {'campo1': 2, 'campo2': 3}
}
"""