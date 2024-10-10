import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image

imagen_color = Image.open("planta.png")
imagen_np = np.array(imagen_color)
print(imagen_np)

imagen_desenfocada = ndimage.gaussian_filter(imagen_np, sigma=50)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(imagen_np)

plt.subplot(1, 2, 2)
plt.title("Imagen Desenfocada")
plt.imshow(imagen_desenfocada)

plt.show()