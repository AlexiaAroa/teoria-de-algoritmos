from grafo import Grafo
# devolver n d-s de dicho grafo de  a lo sumo k vertices

def dominating_set(grafo, k, solucion, i_act, vertices):
    if len(solucion) == k:
        if es_compatible(grafo, solucion, vertices):
            return True, solucion
        else:
            return False, None
        
    if len(solucion) < k and es_compatible(grafo, solucion, vertices):
        return True, solucion
    
    if i_act == len(vertices):
        return False, None
    
    vertice_actual = vertices[i_act]
    solucion.append(vertice_actual)
    if dominating_set(grafo, k, solucion, i_act + 1, vertices)[0]:
        return True, solucion
    
    solucion.pop()
    return dominating_set(grafo, k, solucion, i_act + 1, vertices)


def es_compatible(grafo, solucion, vertices):
    visitados = set()

    for v in solucion:
        visitados.add(v)
        for w in grafo.adyacentes(v):
            visitados.add(w)

    return len(vertices) == len(visitados)        
    
# ------------------------------------------------------------------------    
grafo_lista_enlazada = Grafo()
grafo_lista_enlazada.agregar_vertice("A")
grafo_lista_enlazada.agregar_vertice("B")
grafo_lista_enlazada.agregar_vertice("C")
grafo_lista_enlazada.agregar_vertice("D")
grafo_lista_enlazada.agregar_arista("A", "B")
grafo_lista_enlazada.agregar_arista("B", "C")
grafo_lista_enlazada.agregar_arista("C", "D")


solucion_no = dominating_set(grafo_lista_enlazada, 1, [], 0, grafo_lista_enlazada.obtener_vertices())
print(solucion_no)

solucion_si = dominating_set(grafo_lista_enlazada, 3, [], 0, grafo_lista_enlazada.obtener_vertices())
print(solucion_si)



grafo_prueba1 = Grafo()
grafo_prueba1.agregar_vertice("A")
grafo_prueba1.agregar_vertice("B")
grafo_prueba1.agregar_vertice("C")
grafo_prueba1.agregar_vertice("D")
grafo_prueba1.agregar_vertice("E")
grafo_prueba1.agregar_arista("A", "B")
grafo_prueba1.agregar_arista("A", "C")
grafo_prueba1.agregar_arista("B", "D")
grafo_prueba1.agregar_arista("C", "D")
grafo_prueba1.agregar_arista("C", "E")
grafo_prueba1.agregar_arista("D", "E")


solucion2 = dominating_set(grafo_prueba1, 3, [], 0, grafo_prueba1.obtener_vertices())
print(solucion2)