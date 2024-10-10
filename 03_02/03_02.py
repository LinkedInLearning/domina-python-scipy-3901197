import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

tasa_muestreo = 1000 

tiempo_total = 1.0 
t = np.linspace(0.0, tiempo_total, int(tasa_muestreo * tiempo_total), endpoint=False)

frecuencia_guitarra = 150 
frecuencia_bajo = 60
sonido = np.sin(frecuencia_guitarra * 2.0 * np.pi * t) + 0.5 * np.sin(frecuencia_bajo * 2.0 * np.pi * t)
