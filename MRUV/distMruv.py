def distMruv(v0, a, t):
    return v0*t + (a*t**2)/2

velInicial = float(input("Ingresa la velocidad inicial: "))
aceleracion = float(input("Ingresa la aceleración: "))
tiempo = float(input("Ingresa el tiempo: "))

d = distMruv(velInicial, aceleracion, tiempo)

print("La distancia recorrida es: {:.2f}".format(d))