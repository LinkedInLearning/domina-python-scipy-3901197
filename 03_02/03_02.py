import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

tasa_muestreo = 1000 

tiempo_total = 1.0 
t = np.linspace(0.0, tiempo_total, int(tasa_muestreo * tiempo_total), endpoint=False)

frecuencia_guitarra = 150 
frecuencia_bajo = 60
sonido = np.sin(frecuencia_guitarra * 2.0 * np.pi * t) + 0.5 * np.sin(frecuencia_bajo * 2.0 * np.pi * t)

yf = fft(sonido)
xf = fftfreq(int(tasa_muestreo * tiempo_total), 1/tasa_muestreo)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, sonido)
plt.title("Sonido de la Guitarra y el Bajo en el Tiempo")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")

plt.subplot(2, 1, 2)
plt.plot(xf[:tasa_muestreo//2], np.abs(yf[:tasa_muestreo//2]))
plt.title("Transformada Rápida de Fourier (Frecuencias)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.grid()
plt.subplots_adjust(hspace=0.5)
plt.show()
