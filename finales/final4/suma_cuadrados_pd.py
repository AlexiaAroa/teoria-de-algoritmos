# Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
# utilizando programación dinámica. Indicar y justificar el orden del algoritmo implementado.
# Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1**2, por lo que siempre existe solución.
# Sin embargo, la expresión 10 = 3**2 + 1**2 es una manera más económica de escribirlo para n = 10, 
# pues sólo tiene dos términos. Además, tener en cuenta que no se piden los términos, 
# sino la cantidad mínima de términos cuadráticos necesaria.

def suma_cuadrados(n):
    cuadrados = armar_sistema(n)
    optimos = [0] * (n + 1)
    for i in range(1, n + 1):
        minimo = i
        for valor in cuadrados:
            if valor <= i:
                cantidad = 1 + optimos[i - valor]
                if cantidad < minimo:
                    minimo = cantidad

        optimos[i] = minimo

    return optimos[n]



def armar_sistema(n):
    sistema = []
    for i in range(1, n):
        if i ** 2 > n:
            break
        
        sistema.append(i ** 2)
    
    return sistema

########################################################
print(suma_cuadrados(10))