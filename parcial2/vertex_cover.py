from grafo import Grafo

# Version 1 ------------------------------------------------------------------
def _minimo_vertex_cover(grafo, vertices, i_act, solucion_minima, solucion_actual):
    if cubre_todas_las_aristas(grafo, solucion_actual):
        if solucion_minima == [] or len(solucion_actual) < len(solucion_minima):
            actualizar_solucion_minima(solucion_minima, solucion_actual)
            return
        
    if i_act >= len(vertices):
        return

    vertice_actual = vertices[i_act]
    solucion_actual.append(vertice_actual)
    _minimo_vertex_cover(grafo, vertices, i_act + 1, solucion_minima, solucion_actual) 
    solucion_actual.pop()
    _minimo_vertex_cover(grafo, vertices, i_act + 1, solucion_minima, solucion_actual)

def minimo_vertex_cover(grafo):
    minimo = []
    _minimo_vertex_cover(grafo, grafo.obtener_vertices(), 0, minimo, [])
    return minimo

def cubre_todas_las_aristas(grafo, solucion):
    visitados = set()

    for v in solucion:
        visitados.add(v)
        for w in grafo.adyacentes(v):
            visitados.add(w)

    return len(visitados) == len(grafo.obtener_vertices())

def actualizar_solucion_minima(solucion_minima, solucion_actual):
    solucion_minima.clear()
    for v in solucion_actual:
        solucion_minima.append(v)

# Version 2 ------------------------------------------------------------------

def _minimo_vertex_cover_v2(grafo, vertices, i_act, solucion_actual):
    if cubre_todas_las_aristas(grafo, solucion_actual):
        return [set(solucion_actual)]
        
    if i_act >= len(vertices):
        return []
    
    vertice_actual = vertices[i_act]
    solucion_actual.append(vertice_actual)
    s_con = _minimo_vertex_cover_v2(grafo, vertices, i_act + 1, solucion_actual)
    solucion_actual.pop()
    s_sin = _minimo_vertex_cover_v2(grafo, vertices, i_act + 1, solucion_actual)
    return s_con + s_sin

def minimo_vertex_cover_v2(grafo):
    soluciones = _minimo_vertex_cover_v2(grafo, grafo.obtener_vertices(), 0, [])
    return min(soluciones, key=len)

# ------------------------------------------------------------------------
grafo_lista_enlazada = Grafo()
grafo_lista_enlazada.agregar_vertice("A")
grafo_lista_enlazada.agregar_vertice("B")
grafo_lista_enlazada.agregar_vertice("C")
grafo_lista_enlazada.agregar_vertice("D")
grafo_lista_enlazada.agregar_arista("A", "B")
grafo_lista_enlazada.agregar_arista("B", "C")
grafo_lista_enlazada.agregar_arista("C", "D")

# print(minimo_vertex_cover(grafo_lista_enlazada))

print(minimo_vertex_cover_v2(grafo_lista_enlazada))