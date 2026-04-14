import networkx as nx

# Crear un grafo dirigido con pesos
G = nx.DiGraph()
G.add_weighted_edges_from([
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
])

# Calcular el camino más corto desde el nodo 'A'
distancias = nx.single_source_dijkstra_path_length(G, 'A')
print(distancias)