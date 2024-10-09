from scipy.spatial import distance

ubicacion_maria = [2, 3]
ubicacion_ana = [5, 1]

cafe_1 = [3, 2]
cafe_2 = [6, 3]

distancia_maria_cafe1 = distance.euclidean(ubicacion_maria, cafe_1)
print("Distancia entre María y el Café 1:", distancia_maria_cafe1)

distancia_ana_cafe1 = distance.euclidean(ubicacion_ana, cafe_1)
print("Distancia entre Ana y el Café 1:", distancia_ana_cafe1)

distancia_maria_cafe2 = distance.euclidean(ubicacion_maria, cafe_2)
print("Distancia entre María y el Café 2:", distancia_maria_cafe2)

distancia_ana_cafe2 = distance.euclidean(ubicacion_ana, cafe_2)
print("Distancia entre Ana y el Café 2:", distancia_ana_cafe2)


distancia_total_cafe1 = distancia_maria_cafe1 + distancia_ana_cafe1
distancia_total_cafe2 = distancia_maria_cafe2 + distancia_ana_cafe2

if distancia_total_cafe1 < distancia_total_cafe2:
    print("El Café 1 es el punto de encuentro más cercano para Ana y María.")
else:
    print("El Café 2 es el punto de encuentro más cercano para Ana y María.")
