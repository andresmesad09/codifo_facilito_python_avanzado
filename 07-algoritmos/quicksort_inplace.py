def quicksort_inplace(arr, low, high):
    if low < high:
        # Particionar la lista y obtener el índice del pivote
        pi = partition(arr, low, high)
        # Ordenar las sublistas
        
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    
    pivot = arr[high]  # Elegir el pivote (último elemento)
    i = low - 1  # Índice del elemento más pequeño
    print(i)
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiar elementos
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Mover el pivote a su lugar
    return i + 1

# Ejemplo de uso
lista = [3, 6, 8, 10, 1, 2, 1]
quicksort_inplace(lista, 0, len(lista) - 1)
print("Lista ordenada:", lista)
