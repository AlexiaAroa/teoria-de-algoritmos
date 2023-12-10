# Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos 
# a todos. Implementar un algoritmo que dé la cantidad mínima de faros que se necesitan para que todos 
# los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes
# (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”).
VACIO = 0
SUBMARINO = 1
FARO = 2

# ENCUENTRA TODAS LAS SOLUCIONES !

def submarinos(matriz, solucion, fila, columna, cant_faros):
    if fila == -1 or columna == -1:
        return
    
    # print("fila", fila, " col", columna, " valor", matriz[fila][columna])

    if ilumina_todos_los_submarinos(matriz):
        solucion.append(cant_faros[:])
        return
    
    if not ilumina_submarino(matriz, fila, columna):
        fila, columna = siguiente_posicion_a_analizar(matriz, fila, columna, True)
        submarinos(matriz, solucion, fila, columna, [cant_faros[0]])
        return
    
    matriz_anterior = duplicar_grilla(matriz) # me guardo el estado
    matriz[fila][columna] = FARO

    iluminar_zona(matriz, fila, columna)
    fila_n, columna_n = siguiente_posicion_a_analizar(matriz, fila, columna)
    submarinos(matriz, solucion, fila_n, columna_n, [cant_faros[0] + 1])
    
    # vuelvo al estado anterior
    fila_p, columna_p = siguiente_posicion_a_analizar(matriz_anterior, fila, columna, True)
    submarinos(matriz_anterior, solucion, fila_p, columna_p, [cant_faros[0]])

def ilumina_todos_los_submarinos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == SUBMARINO:
                return False
            
    return True

def iluminar_zona(matriz, fila, columna):
    fila_iniciar = max(0, fila - 2)
    columna_iniciar = max(0, columna - 2)
    fila_fin = min(len(matriz), fila + 3)
    columna_fin = min(len(matriz[0]), columna + 3)

    for i in range(fila_iniciar, fila_fin):
        for j in range(columna_iniciar, columna_fin):
            matriz[i][j] = FARO


def siguiente_posicion_a_analizar(matriz, fila, columna, skip = False):
    for i in range(fila, len(matriz)):
        for j in range(columna, len(matriz[i])):
            if matriz[i][j] != FARO and not skip:
                return i, j
            
            skip = False
            
        columna = 0

    return -1, -1

def ilumina_submarino(matriz, fila, columna):
    fila_iniciar = max(0, fila - 2)
    columna_iniciar = max(0, columna - 2)
    fila_fin = min(len(matriz), fila + 3)
    columna_fin = min(len(matriz[0]), columna + 3)

    for i in range(fila_iniciar, fila_fin):
        for j in range(columna_iniciar, columna_fin):
            if matriz[i][j] == SUBMARINO:
                return True
    return False

def duplicar_grilla(grilla):
    return [fila.copy() for fila in grilla]


# Caso visto en clase

matriz = [     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
soluciones = []
submarinos(matriz, soluciones, 0, 0, [0])

print("sol", soluciones)