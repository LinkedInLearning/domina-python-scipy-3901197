import numpy as np
from scipy import stats

grupo_vitamina = [1.1, 2.3, 1.8, 2.5, 2.2, 3.0, 2.9, 3.1, 2.8, 3.3]
grupo_agua = [0.5, 0.6, 0.4, 0.8, 0.5, 0.7, 0.9, 0.6, 0.8, 0.5]

t_prueba, p_valor = stats.ttest_ind(grupo_vitamina, grupo_agua)

print(f"Estadístico t: {t_prueba}")
print(f"P-valor: {p_valor}")

if p_valor < 0.05:
    print("La diferencia entre los grupos es significativa.")
else:
    print("No hay una diferencia significativa entre los grupos.")
