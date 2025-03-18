"""
Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una
misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso
está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. Por problemas presupuestarios, sólo
pueden pintar los colectivos de k colores diferentes (por ejemplo, k = 4, pero podría se otro valor). Como no quieren
parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber si es posible
cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma que no hayan dos de mismo color
coincidiendo en la misma parada). Considerando que se tiene la información de todas las paradas de colectivo y qué
líneas paran allí, modelar el problema utilizando grafos e implementar un algoritmo que determine si es posible resolver
el problema. Indicar la complejidad del algoritmo implementado.

Creación grafo

Vértices: líneas del colectivo
Aristas: conexiones entre las líneas de colectivo -> en caso de que pertenezcan a una misma parada

"""

def coloreo_colectivos(grafo, vertices, i_act, k, colores):
    if i_act >= len(vertices):
        return True, colores
    
    v = vertices[i_act]

    for i in range(k):
        colores[v] = i # pinto la linea
        if not es_compatible(grafo, v, colores): # si en una misma parada tienen dos lineas el mismo color
            continue # pruebo pintando con otro color

        if coloreo_colectivos(grafo, vertices, i_act + 1, k, colores)[0]:
            return True, colores
        
    # si pinte con todos los colores y no encuentro la solucion
    return False, None


def es_compatible(grafo, v, colores):
    for w in grafo.adyacentes(v):
        if w in colores and colores[w] == colores[v]:
            return False
        
    return True
