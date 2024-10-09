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

print("Número de elementos no cero:", matriz_csr.count_nonzero())

matriz_csr[1, 1] = 0

print("Matriz CSR después de ingresar un valor 0:", matriz_csr)

print("Número de elementos no ceros:", matriz_csr.nnz)

matriz_csr.eliminate_zeros()

print("Matriz CSR después de eliminar ceros:", matriz_csr)

print("Número de elementos no ceros:", matriz_csr.nnz)
