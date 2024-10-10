import numpy as np
from scipy import stats

horas_estudio = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
notas_examen = [50, 55, 60, 65, 70, 75, 78, 82, 85, 88]

pendiente_linea_regresion, interseccion, r_valor, p_valor, std_err = stats.linregress(horas_estudio, notas_examen)

print(f"Pendiente: {pendiente_linea_regresion}")
print(f"Intersección: {interseccion}")
print(f"Valor R-cuadrado: {r_valor**2}")
print(f"P-valor: {p_valor}")

horas_futuras = 15
nota_predicha = pendiente_linea_regresion * horas_futuras + interseccion
print(f"Predicción de nota con {horas_futuras} horas de estudio: {nota_predicha}")
