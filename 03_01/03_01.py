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
