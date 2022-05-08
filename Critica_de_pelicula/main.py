import functools

def main():
    datos = {
        5 : 40,
        4 : 99,
        3 : 145,
        2 : 133,
        1 : 96,
        0 :40
    }

    N = functools.reduce(lambda x, y: x + y, list(datos.values()))

    productos = list(map(lambda x: x*datos[x], datos))

    media = functools.reduce(lambda x, y: x+y, productos)/N

    datos_cuadrados = list(map(lambda x: datos[x]*((x-media)**2), datos))

    varianza = functools.reduce(lambda x, y: x+y, datos_cuadrados)/N

    desviacion_tipica = varianza**(1/2)

    print("Media:", media)
    print("Varianza:", varianza)
    print("Desviación Típica:", desviacion_tipica)

    Intervalo_68 = [media-desviacion_tipica, media+desviacion_tipica]
    Intervalo_95= [media-2*desviacion_tipica, media+2*desviacion_tipica]
    Intervalo_99= [media-3*desviacion_tipica, media+3*desviacion_tipica]

    print("Intervalo 68% :", Intervalo_68)
    print("Intervalo_95% :", Intervalo_95)
    print("Intervalo 99,7% :", Intervalo_99)


if __name__ == '__main__':
    main()


