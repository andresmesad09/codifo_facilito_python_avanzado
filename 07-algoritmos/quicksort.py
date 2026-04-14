def quicksort(arr):
    # Caso base: una lista de 0 o 1 elementos está ordenada
    if len(arr) <= 1:
        return arr
    else:
        # Elegir el pivote (en este caso el elemento central de la lista)
        pivot = arr[len(arr) // 2]
        # Particionar la lista en tres sublistas
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Ordenar las sublistas y concatenarlas
        print("pivot: ",pivot," quicksort: ",left," middle: " ,middle, " quicksort: ", right)
        return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso
lista = [3, 6, 8, 10, 1, 2, 1]

print("Lista ordenada:", quicksort(lista))

