from scipy.integrate import dblquad

#f(x, y) = x^2 + y^2
def funcion_terreno(x, y):
    return x**2 + y**2

resultado, error = dblquad(funcion_terreno, 0, 2, lambda x: 0, lambda x: 1)

print(f"El volumen total de tierra que necesita ser nivelado es: {resultado} unidades cúbicas")
print(f"Error estimado del cálculo: {error}")
