import math

def calcular_zona_fresnel(d, f):
    """
    Calcula la zona de Fresnel en base a la fórmula: f1[m] = 8.656 * sqrt(d/f)
    
    :param d: Distancia en kilómetros
    :param f: Frecuencia en gigahertz
    :return: Tamaño de la zona de Fresnel en metros
    """
    f1 = 8.656 * math.sqrt(d / f)
    return f1

# Solicitar la distancia y la frecuencia al usuario
distancia_km = float(input("Ingrese la distancia en kilómetros: "))
frecuencia_ghz = float(input("Ingrese la frecuencia en gigahertz: "))

# Calcular la zona de Fresnel utilizando la función
zona_fresnel = calcular_zona_fresnel(distancia_km, frecuencia_ghz)

# Mostrar el resultado
print(f"La zona de Fresnel es de {zona_fresnel:.2f} metros.")   # el :.2f se utiliza para poder redondear el resultado para el usuario

