from scipy.integrate import quad

#f(t) = 2t^2 + 3t + 1
def velocidad(t):
    return 2*t**2 + 3*t + 1

resultado, error = quad(velocidad, 0, 5)

print(f"El volumen total de agua: {resultado} unidades cúbicas")
print(f"Error estimado: {error}")
