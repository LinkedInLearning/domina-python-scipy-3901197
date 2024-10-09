import numpy as np
from scipy.sparse import csr_matrix

datos = [1, 2, 3, 4]
indices_columnas = [0, 2, 2, 0]
indptr = [0, 2, 3, 4]

matriz_csr = csr_matrix((datos, indices_columnas, indptr), shape=(3, 3))
print("Matriz CSR original:") 
print(matriz_csr.toarray())

matriz_transpuesta = matriz_csr.transpose()

print("Matriz transpuesta:")
print(matriz_transpuesta.toarray())
