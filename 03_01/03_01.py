import numpy as np
from scipy.cluster.hierarchy import fcluster, linkage
import matplotlib.pyplot as plt

usuarios = np.array([
    [3, 10],  
    [4, 12],  
    [5, 9],   
    [15, 3],  
    [14, 4],  
    [16, 5],  
    [25, 1],  
    [24, 2],  
    [26, 1] 
])

Z = linkage(usuarios, method='ward')

clustering = fcluster(Z, 3, criterion='maxclust')

print("Clústeres asignados a los usuarios:", clustering)

plt.scatter(usuarios[:,0], usuarios[:,1], c=clustering, cmap='rainbow')
plt.title("Agrupación de Usuarios")
plt.xlabel("Horas viendo películas")
plt.ylabel("Horas viendo series")
plt.show()
