import numpy as np
from scipy.sparse import csr_matrix

datos_originales = np.array([
    [0, 0, 3],
    [4, 0, 0],
    [0, 1, 0],
    [3, 0, 5]
])

matriz_csr = csr_matrix(datos_originales)

print("Matriz original")
print(datos_originales)

print("Matriz CSR:", matriz_csr)
