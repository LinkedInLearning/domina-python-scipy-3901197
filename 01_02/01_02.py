import numpy as np
from scipy.sparse import csr_matrix

datos_usuarios = [1, 2, 3, 4]
indices_columna_usuarios = [0, 2, 2, 0]
indptr_usuarios = [0, 2, 3, 4]

matriz_usuarios = csr_matrix((datos_usuarios, indices_columna_usuarios, indptr_usuarios), shape=(3, 3))

datos_productos = [5, 6, 7]
indices_columna_productos = [1, 0, 2]
indptr_productos = [0, 1, 2, 3]

matriz_productos = csr_matrix((datos_productos, indices_columna_productos, indptr_productos), shape=(3, 3))

sum_matriz = matriz_usuarios + matriz_productos

mult_matriz = matriz_usuarios.dot(matriz_productos)

print("Suma de matrices CSR:")
print(sum_matriz.toarray())

print("Multiplicación de matrices CSR:")
print(mult_matriz.toarray())
