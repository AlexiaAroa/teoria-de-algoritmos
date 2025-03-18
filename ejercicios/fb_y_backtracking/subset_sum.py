def subset_sum_bt(numeros, valor, solucion, solucion_parcial, i_act):
    if sum(solucion_parcial) == valor:
        solucion.append(solucion_parcial[:])
        return
    
    if sum(solucion_parcial) > valor:
        return

    for i in range(i_act, len(numeros)):
        solucion_parcial.append(numeros[i])
        subset_sum_bt(numeros, valor, solucion, solucion_parcial, i_act + i)
        solucion_parcial.pop()


numeros = [5, 6, 8, 9, 3, 2]
soluciones = []
subset_sum_bt(numeros, 24, soluciones, [], 0)
print(soluciones)


def subset_sum_bt_v2(numeros, valor, solucion, solucion_parcial, i_act):
    if sum(solucion_parcial) > valor:
        return

    if sum(solucion_parcial) == valor:
        solucion.append(solucion_parcial[:])
        return

    if i_act >= len(numeros):
        if len(solucion) == 0 or sum(solucion_parcial) > sum(solucion[0]):
            solucion.append(solucion_parcial[:])
        return
    
    numero_actual = numeros[i_act]
    solucion_parcial.append(numero_actual)
    subset_sum_bt_v2(numeros, valor, solucion, solucion_parcial, i_act + 1)
    solucion_parcial.pop()
    subset_sum_bt_v2(numeros, valor, solucion, solucion_parcial, i_act + 1)

soluciones2 = []
subset_sum_bt_v2(numeros, 15, soluciones2, [], 0)
print(soluciones2)