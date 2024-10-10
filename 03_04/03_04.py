import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image

imagen_color = Image.open("planta.png")
imagen_np = np.array(imagen_color)
print(imagen_np)