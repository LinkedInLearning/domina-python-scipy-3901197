from scipy.integrate import romberg

# f(t) = 3t^2 + 2t + 1
def consumo_combustible(t):
    return 3*t**2 + 2*t + 1

resultado = romberg(consumo_combustible, 0, 15)

print(f"El consumo total de combustible en los primeros 15 segundos es: {resultado }litros")