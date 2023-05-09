def distanciaMRU(v, t):
    return v * t

velocidad = float(input("Introduce la velocidad: "))
tiempo = float(input("Introduce el tiempo: "))

d = distanciaMRU(velocidad, tiempo)

print("La distancia recorrida es: {:.2f}".format(d))
