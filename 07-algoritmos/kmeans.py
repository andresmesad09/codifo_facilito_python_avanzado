# Importar las bibliotecas necesarias
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generar datos de ejemplo
from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Crear y ajustar el modelo K-means
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Obtener los centroides y las etiquetas de los clústeres
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Visualizar los resultados
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, marker='X')  # Centroides
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-means Clustering')
plt.show()