# Barrio circular
# Robar la casa -> Obtengo su ganancia y no puedo robar a los vecinos
# Si no robo la casa -> No gano nada, me quedo con el optimo del vecino anterior
ARREGLO_OPTIMO = 0
VALOR_OPTIMO = 1

def ladron_lunatico(valores, nro_casa):
    optimos = [0] * (nro_casa)

    optimos[0] = valores[0]
    optimos[1] = max(valores[1], valores[0])

    for i in range(2, nro_casa):
        optimos[i] = max(valores[i] + optimos[i - 2], optimos[i - 1])

    return optimos, optimos[nro_casa - 1]

def reconstruir_solucion(arreglo_optimos, valores, nro_casa, solucion):
    if nro_casa == 0:
        solucion.append(nro_casa)
        return solucion

    if nro_casa < 2: # casa 1 y casa 2
        if arreglo_optimos[1] == valores[1]:
            solucion.append(1)
        else:
            solucion.append(0)

        return solucion

    if valores[nro_casa] + arreglo_optimos[nro_casa - 2] >= arreglo_optimos[nro_casa - 1]:
        solucion.append(nro_casa)
        return reconstruir_solucion(arreglo_optimos, valores, nro_casa - 2, solucion)

    return reconstruir_solucion(arreglo_optimos, valores, nro_casa - 1, solucion)

# Si robo la primera casa, ya no puedo robar la ultima, porque se va a enterar
# Si robo la segunda casa, puedo tener la oportunidad de robar la ultima

valores_casas = [80, 40, 10, 100, 30, 20]

robando_primera_casa = ladron_lunatico(valores_casas[:-1], len(valores_casas) - 1)
robando_ultima_casa = ladron_lunatico(valores_casas[1:], len(valores_casas) - 1)

if robando_primera_casa[VALOR_OPTIMO] > robando_ultima_casa[VALOR_OPTIMO]:
    print(robando_primera_casa[VALOR_OPTIMO])
    solucion = reconstruir_solucion(robando_primera_casa[ARREGLO_OPTIMO], valores_casas, len(valores_casas) - 2, [])
else:
    print(robando_ultima_casa[VALOR_OPTIMO])
    solucion = reconstruir_solucion(robando_ultima_casa[ARREGLO_OPTIMO], valores_casas, len(valores_casas) - 2, [])

solucion.reverse()
print(solucion)
