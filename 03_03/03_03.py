import numpy as np
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt
from PIL import Image

imagen_real = Image.open("planta.png")
imagen_real = imagen_real.convert("L")

imagen_np = np.array(imagen_real)
print(imagen_np)