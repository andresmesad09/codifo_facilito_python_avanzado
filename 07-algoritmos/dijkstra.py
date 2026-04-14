import heapq

def dijkstra(graph, start):
    # Inicialización
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distancia, nodo)
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        # Actualización de las distancias a los nodos vecinos
        print("current_node ", current_node)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            print("distance: ",distance)
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
        print("queue: ",priority_queue)

    return distances

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"Distancias desde el nodo {start_node}: {distances}")
