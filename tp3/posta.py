from constantes import conjuntos_5, conjuntos_7, conjuntos_10_pocos

def backtracking_5(conjuntos, solucion_parcial, i_actual, solucion): # [sets] [] int    
    if i_actual == len(conjuntos):
        if es_solucion(solucion_parcial, conjuntos):
            actualizar_solucion_minima(solucion_parcial, solucion)
        return
    
    conjunto_actual = conjuntos[i_actual]
    
    for j in range(len(conjunto_actual)):
        # Agrega el conjunto actual al candidato
        # la poda aca ?

        jugador_actual = conjunto_actual[j]

        if jugador_se_repite(solucion_parcial, jugador_actual):
            continue

        solucion_parcial.append(jugador_actual)

        # Realiza la llamada recursiva, pruebo agregando el elemento
        backtracking_5(conjuntos, solucion_parcial, i_actual + 1, solucion)

         # Realiza la llamada recursiva, quitando el elemento
        solucion_parcial.remove(jugador_actual)

        # Si se encuentra una solución, devuelve el resultado
        backtracking_5(conjuntos, solucion_parcial, i_actual + 1, solucion)

   
def es_solucion(solucion_parcial, conjuntos):
    valor = all(any(element in solucion_parcial for element in s) for s in conjuntos)
    return valor
  
def actualizar_solucion_minima(solucion_parcial, solucion):
    if len(solucion) == 0:
        solucion.append(set(solucion_parcial))
        return
    
    if len(solucion[0]) > len(solucion_parcial):
        solucion.pop()
        solucion.append(set(solucion_parcial))

def jugador_se_repite(solucion_parcial, jugador_actual):
    if len(solucion_parcial) == 0:
        return False
    
    return jugador_actual in set(solucion_parcial) # set O(1)

def hitting_set(sets):
    solucion = []
    backtracking_5(sets, [], 0, solucion)
    return solucion

try:
    resultado = hitting_set(conjuntos_10_pocos)
    print(resultado)

except RecursionError:
    print("Error de recursion")
except MemoryError:
    print("Error de memoria")
