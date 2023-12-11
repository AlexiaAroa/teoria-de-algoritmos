# Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi+1)).
# Cada vertice tiene un valor (positivo).
# Implementar un algoritmo que, utilizando programación dinámica, obtenga el Set Independiente de suma máxima
# dentro de un grafo de dichas características. Indicar y justificar la complejidad del algoritmo implementado.

def independent_set(grafo_vertices):
    if len(grafo_vertices) == 0:
        return [], 0
    
    # está incluido el caso base, 0 vertices, valor 0
    optimos = [0] * len(grafo_vertices)
    optimos[0] = grafo_vertices[0] # si tengo 1 vertice, lo tomo
    optimos[1] = max(grafo_vertices[0], grafo_vertices[1]) # si tengo 2 vertices, tomo el mayor entre los 2

    for i in range(2, len(grafo_vertices)):
        optimos[i] = max(grafo_vertices[i] + optimos[i - 2], optimos[i - 1])

    return optimos, optimos[-1]

def _reconstruir(grafo_vertices, optimos, nro_vertice, solucion):
    if nro_vertice < 0:
        return solucion
    
    if nro_vertice == 0:
        solucion.append(grafo_vertices[nro_vertice])
        return solucion
    
    if nro_vertice == 1: # incluye vertice 1 y 2
        if optimos[nro_vertice] == grafo_vertices[nro_vertice]:
            solucion.append(grafo_vertices[nro_vertice])
        else: 
            solucion.append(grafo_vertices[nro_vertice - 1])

        return solucion
    

    if grafo_vertices[nro_vertice] + optimos[nro_vertice - 2] >= optimos[nro_vertice - 1]:
        solucion.append(grafo_vertices[nro_vertice])
        return _reconstruir(grafo_vertices, optimos, nro_vertice - 2, solucion)

    return _reconstruir(grafo_vertices, optimos, nro_vertice - 1, solucion)

def reconstruir(grafo, optimos):
    solucion = _reconstruir(grafo, optimos, len(grafo) - 1, [])
    solucion.reverse()
    return solucion

# Suponiendo que mi arreglo es mi grafo camino 4 -> 3 -> 2 -> 1
grafo = [4, 3, 2, 1]
solucion = independent_set(grafo)
print(solucion[1])
print(reconstruir(grafo, solucion[0]))