import numpy as np
from scipy.sparse import csr_matrix

calificaciones_peliculas = np.array([
    [5, 0, 0, 0, 3],
    [0, 4, 0, 2, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0],
    [0, 2, 0, 0, 0]
])

matriz_csr = csr_matrix(calificaciones_peliculas)

print("Valores no ceros:", matriz_csr.data)
print("Índices columnas:", matriz_csr.indices)
print("Punteros de filas (indptr):", matriz_csr.indptr)