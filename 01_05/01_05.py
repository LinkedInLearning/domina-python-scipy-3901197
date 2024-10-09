import numpy as np
from scipy.linalg import det

matrix = np.array([
    [4, 2, 3, 1],
    [2, 3, 1, 4],
    [1, 1, 2, 2],
    [2, 3, 2, 4]
])

determinante = det(matrix)

print("El determinante de la matriz es:", determinante)

if np.isclose(determinante, 0):
    print("No tiene una solución única y el puente podría ser inestable.")
else:
    print("El puente es estable.")
