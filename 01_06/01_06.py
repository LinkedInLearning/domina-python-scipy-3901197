import numpy as np
from scipy.linalg import eig

rigidez_edificio = np.array([
    [6, -2, 1],
    [-2, 5, -2],
    [1, -2, 4]
])

eigenvalues, eigenvectors = eig(rigidez_edificio)

print("Valores propios:")
print(eigenvalues)

print("Vectores propios:")
print(eigenvectors)
