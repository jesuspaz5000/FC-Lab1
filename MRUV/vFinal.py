def vFinal(v0, a, t):
    return v0 + a * t

velInicial = float(input("Ingresa la velocidad inicial: "))
aceleracion = float(input("Ingresa la aceleración: "))
tiempo = float(input("Ingresa el tiempo: "))

v = vFinal(velInicial, aceleracion, tiempo)

print("La velocidad final es: {:.2f}".format(v))