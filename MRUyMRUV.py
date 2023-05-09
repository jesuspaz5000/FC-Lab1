continuar = "si"
while(continuar == "si"):
    tipo = float(input("¿Qué tipo de movimiento deseas calcular?\n1. MRU\n2. MRUV\n"))
    if tipo == 1:
        dato = float(input("¿Qué dato deseas calcular?\n1. Distancia\n2. Velocidad\n3. Tiempo\n"))
        if dato == 1:
            velocidad = float(input("Ingresa la velocidad: "))
            tiempo = float(input("Ingresa el tiempo: "))
            d = velocidad * tiempo
            print("La distancia recorrida es: {:.2f}".format(d))
        elif dato == 2:
            distancia = float(input("Ingresa la distancia: "))
            tiempo = float(input("Ingresa el tiempo: "))
            v = distancia / tiempo
            print("La velocidad es: {:.2f}".format(v))
        else:
            distancia = float(input("Ingresa la distancia: "))
            velocidad = float(input("Ingresa la velocidad: "))
            t = distancia / velocidad
            print("El tiempo es: {:.2f}".format(t))
    else:
        dato = float(input("¿Qué dato deseas calcular?\n1. Distancia\n2. Velocidad inicial\n3. Velocidad final\n4. Aceleración\n5. tiempo\n"))
        if dato == 1:
            velocidadInicial = float(input("Ingresa la velocidad inicial: "))
            aceleracion = float(input("Ingresa la aceleración: "))
            tiempo = float(input("Ingresa el tiempo: "))
            d = velocidadInicial * tiempo + (aceleracion * tiempo ** 2) / 2
            print("La distancia recorrida es: {:.2f}".format(d))
        elif dato == 2:
            velocidadFinal = float(input("Ingresa la velocidad final: "))
            aceleracion = float(input("Ingresa la aceleración: "))
            tiempo = float(input("Ingresa el tiempo: "))
            v0 = velocidadFinal - aceleracion * tiempo
            print("La velocidad inicial es: {:.2f}".format(v0))
        elif dato == 3:
            velocidadInicial = float(input("Ingresa la velocidad inicial: "))
            aceleracion = float(input("Ingresa la aceleración: "))
            tiempo = float(input("Ingresa el tiempo: "))
            v = velocidadInicial + aceleracion * tiempo
            print("La velocidad final es: {:.2f}".format(v))
        elif dato == 4:
            velocidadInicial = float(input("Ingresa la velocidad inicial: "))
            velocidadFinal = float(input("Ingresa la velocidad final: "))
            tiempo = float(input("Ingresa el tiempo: "))
            a = (velocidadFinal - velocidadInicial) / tiempo
            print("La aceleración es: {:.2f}".format(a))
        else:
            velocidadInicial = float(input("Ingresa la velocidad inicial: "))
            aceleracion = float(input("Ingresa la aceleración: "))
            velocidadFinal = float(input("Ingresa la velocidad final: "))
            t = (velocidadFinal - velocidadInicial) / aceleracion
            print("El tiempo es: {:.2f}".format(t))
    continuar = input("¿Deseas continuar? (si/no)\n")
    print("\n")
print("¡Hasta luego!\n")