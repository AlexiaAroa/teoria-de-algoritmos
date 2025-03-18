# ' ' esta vacio
# '0' ya lo probé y queda vacio
# '1' hay un faro
# '3' donde ilumina el faro
# '2' hay un submarino

def submarinos(matriz, sig_pos, cant_faros):
    sig_pos = sig_pos_a_usar(matriz, sig_pos)
    fila, columna = sig_pos
    if not posicion_valida(matriz, sig_pos):
        return cant_faros
    
    if not ilumina_submarinos(matriz, sig_pos):
        matriz[fila][columna] = 0
        return submarinos(matriz, sig_pos, cant_faros)
    
    matriz[fila][columna] = 1
    iluminar_zona(matriz, fila, columna)
    solucion_con = submarinos(matriz, (fila, columna), cant_faros + 1)

    apagar_zona(matriz, fila, columna)
    matriz[fila][columna] = 0
    solucion_sin = submarinos(matriz, (fila, columna), solucion_con - 1)

    return max(solucion_con, solucion_sin)


def sig_pos_a_usar(matriz, sig_pos):
    fila, columna = sig_pos
    for i in range(fila, len(matriz)):
        for j in range(columna, len(matriz[i])):
            if matriz[i][j] == "":
                return i, j
            
        columna = 0

    return len(matriz), len(matriz[fila])

def posicion_valida(matriz, sig_pos):
    fila, columna = sig_pos
    return (fila >= 0 and fila < len(matriz)) and (columna > 0 or columna <= len(matriz[fila]))

def ilumina_submarinos(matriz, sig_pos):
    fila, columna = sig_pos

    for i in range(0 if fila <= 2 else fila - 2, fila if fila + 2 > len(matriz) else fila + 2): # +3 asi lo incluye
        for j in range(0 if columna <= 2 else columna - 2, columna if columna + 2 > len(matriz[fila]) else columna + 2):
            if matriz[i][j] == "2":
                return True
            
    return False
    

def iluminar_zona(matriz, fila, columna):
    if fila <= 2:
        f_inicio = 0
    else:
        f_inicio = fila - 2

    if fila + 2 >= len(matriz):
        f_fin = len(matriz) - 1
    else:
        f_fin = fila + 2

    if columna + 2 >= len(matriz[fila]):
        col_fin = len(matriz[fila]) - 1
    else:
        col_fin = columna + 2

    for i in range(f_inicio, f_fin + 1):
        for j in range(0 if columna <= 2 else columna - 2, col_fin + 1):
            if matriz[i][j] == "":
                matriz[i][j] = "3"
            
    

def apagar_zona(matriz, fila, columna):

    if fila <= 2:
        f_inicio = 0
    else:
        f_inicio = fila - 2

    if fila + 2 >= len(matriz):
        f_fin = len(matriz) - 1
    else:
        f_fin = fila + 2

    if columna + 2 >= len(matriz[fila]):
        col_fin = len(matriz[fila]) - 1
    else:
        col_fin = columna + 2

    for i in range(f_inicio, f_fin + 1): # +3 asi lo incluye
        for j in range(0 if columna <= 2 else columna - 2, col_fin + 1):
            if matriz[i][j] == "3":
                matriz[i][j] = ""


def main():
    matriz = [[""] * 3 for _ in range(3)]
    matriz[1][0] = "2"

    matriz_10 = [[""] * 10 for _ in range(10)]
    matriz_10[5][6] = "2"




    print(f"3X3: {submarinos(matriz, (0, 0), 0)}")
    print(f"10X10: {submarinos(matriz_10, (0, 0), 0)}")

main()