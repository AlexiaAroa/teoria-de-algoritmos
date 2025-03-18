# Resolver el problema del ejercicio 1 (Bodegon PD) utilizando Backtracking.

def _bodegon(P, w_lugares, i_act, solucion, solucion_parcial):
    if sum(solucion_parcial) > w_lugares:
        return
    
    if sum(solucion_parcial) == w_lugares:
        solucion[0] = solucion_parcial[:]
        return
    
    if i_act >= len(P):
        if len(solucion[0]) == 0 or sum(solucion_parcial) > sum(solucion[0]):
            solucion[0] = solucion_parcial[:]
        return
    
    grupo_actual = P[i_act]
    solucion_parcial.append(grupo_actual)
    _bodegon(P, w_lugares, i_act + 1, solucion, solucion_parcial)   
    solucion_parcial.pop()
    _bodegon(P, w_lugares, i_act + 1, solucion, solucion_parcial)


def bodegon(P, w_lugares):
    solucion = [[]]
    _bodegon(P, w_lugares, 0, solucion, [])
    return solucion[0]

res = bodegon([1, 3, 4, 5], 11)
print(f"Grupos con valores: {res} ocupan {sum(res)} lugares")



# def _bodegon(P, w_lugares, i_act, solucion, solucion_parcial):
#     if sum(solucion_parcial) > w_lugares:
#         return
    
#     if sum(solucion_parcial) == w_lugares:
#         if len(solucion) == 0:
#             solucion.append(solucion_parcial[:])
#         return
    
#     if i_act >= len(P):
#         if len(solucion) == 0:
#             solucion.append(solucion_parcial[:])
#             return
#         if sum(solucion_parcial) > sum(solucion[0]):
#             solucion.pop()
#             solucion.append(solucion_parcial[:])
#         return
    
#     grupo_actual = P[i_act]
#     solucion_parcial.append(grupo_actual)
#     _bodegon(P, w_lugares, i_act + 1, solucion, solucion_parcial)   
#     solucion_parcial.pop()
#     _bodegon(P, w_lugares, i_act + 1, solucion, solucion_parcial)
