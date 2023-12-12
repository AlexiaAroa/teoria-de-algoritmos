# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren
# sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en
# un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se
# trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden
# sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan
# la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar
# y justificar la complejidad del algoritmo.

def bodegon(P, w_lugares):
    matriz = [[0] * (w_lugares + 1) for _ in range(len(P) + 1)]

    for i in range(1, len(P) + 1):
        for j in range(1, w_lugares + 1):
            if P[i - 1] >= j:
                matriz[i][j] = matriz[i - 1][j]
                continue
 
            matriz[i][j] = max(P[i - 1] + matriz[i - 1][j - P[i - 1]], matriz[i - 1][j])

    return reconstruir(matriz, P, w_lugares)

def _reconstruir(matriz, P, w_lugares, solucion, nro_grupo):
    if nro_grupo < 0:
        return solucion
    
    if P[nro_grupo] <= w_lugares and P[nro_grupo] + matriz[nro_grupo - 1][w_lugares - P[nro_grupo]] >= matriz[nro_grupo - 1][w_lugares]:
        solucion.append(nro_grupo)
        return _reconstruir(matriz, P, w_lugares - P[nro_grupo], solucion, nro_grupo - 1)
    
    return _reconstruir(matriz, P, w_lugares, solucion, nro_grupo - 1)


def reconstruir(matriz, P, w_lugares):
    solucion = _reconstruir(matriz, P, w_lugares, [], len(P) - 1)
    solucion.reverse()
    return solucion


# -------------------------------------------------------


print(f"Grupos: {bodegon([1, 3, 4, 5], 10)}")