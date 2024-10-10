import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt

escuelas = np.array([
    [37.77, -122.42], 
    [37.78, -122.43], 
    [37.76, -122.45], 
    [37.79, -122.40] 
])

hospitales = np.array([
    [37.80, -122.41], 
    [37.74, -122.44],
])

distancias_escuela_hospital_1 = distance.cdist(escuelas, [hospitales[0]], 'euclidean')

print("Distancias entre las escuelas y el Hospital 1:")
print(distancias_escuela_hospital_1)

plt.figure(figsize=(8, 6))
plt.scatter(escuelas[:, 1], escuelas[:, 0], color='blue', label='Escuelas', marker='o')
plt.scatter(hospitales[:, 1], hospitales[:, 0], color='red', label='Hospitales', marker='x')
plt.title("Distribución de Escuelas y Hospitales")
plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.legend()
plt.show()
