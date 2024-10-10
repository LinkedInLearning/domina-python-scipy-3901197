import numpy as np
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt
from PIL import Image

imagen_real = Image.open("planta.png")
imagen_real = imagen_real.convert("L")

imagen_np = np.array(imagen_real)
print(imagen_np)

dct_imagen = dct(dct(imagen_np.T, norm='ortho').T, norm='ortho')

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Transformada de Coseno Discreta")
plt.imshow(dct_imagen, cmap='gray')
plt.colorbar()

dct_imagen_comprimida = dct_imagen.copy()
dct_imagen_comprimida[50:, 50:] = 0 

imagen_comprimida = idct(idct(dct_imagen_comprimida.T, norm='ortho').T, norm='ortho')

plt.subplot(1, 2, 2)
plt.title("Imagen Comprimida")
plt.imshow(imagen_comprimida, cmap='gray')
plt.colorbar()
plt.show()