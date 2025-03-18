# No quiere trabajar dos dias seguidos
# Dado un arreglo con el monto esperado a ganar, determinar por PD el maximo monto a ganar

def juan_el_vago(montos, dia):
    if len(montos) == 0 or dia < 0:
        return 0
    
    return max(juan_el_vago(montos, dia - 1), juan_el_vago(montos, dia - 2) + montos[dia])


def juan_el_vago_iter(montos, dia):
    if dia < 0:
        return 0
    
    arreglo = [None] * (dia + 1)
    arreglo[0] = montos[0]
    arreglo[1] = max(montos[0], montos[1])

    for d in range(2, dia + 1):
        arreglo[d] = max(arreglo[d - 1], arreglo[d - 2] + montos[d])

    return arreglo[dia], arreglo


def juan_el_vago_con_caso_base(montos, dia):
    if dia == 0:
        return 0

    arreglo = [0] * (dia + 1)
    arreglo[1] = montos[0] # DIA 1, trabajar y ganar ese dia, o no trabajar y quedar en 0

    for d in range(2, dia + 1):
        # si yo agrego el caso base de dia 0 en arreglo de montos y en el arreglo de optimos
        # entonces, no tendria necesidad de poner montos d-1

        # ahora, si los montos no incluye el caso base, pero, en el arreglo de los optimos si lo incluyo
        # entonces, ahi si tengo que poner el montos d-1 para que se corresponda

        # ahora, si yo no agrego el caso base en los optimos, y tampoco en el arreglo de montos
        # entonces se respeta ec de rec y no hago el d-1
        arreglo[d] = max(montos[d - 1] + arreglo[d - 2], arreglo[d - 1])

    return arreglo[dia], arreglo


def reconstruir_solucion(arreglo, dia, montos, solucion):
    if dia == 1: # dia 1 (posicion 0) y 2 (posicion 1)
        if arreglo[dia] == montos[dia]: # significa que trabajo el dia 2 y no el dia 1
            solucion.append(dia)
        else: # significa que trabajo el dia 1, pero no el dia 2
            solucion.append(0)

    if dia < 2:
        return solucion
    
    if montos[dia] + arreglo[dia - 2] >= arreglo[dia - 1]:
        solucion.append(dia)
        return reconstruir_solucion(arreglo, dia - 2, montos, solucion)
    
    return reconstruir_solucion(arreglo, dia - 1, montos, solucion)

def juan_el_vago_sin_caso_base(montos, dia):
    if dia == 0:
        return 0

    arreglo = [0] * (dia)
    arreglo[0] = montos[0] # DIA 1, trabajar y ganar ese dia, o no trabajar y quedar en 0
    arreglo[1] = max(montos[0], montos[1])

    for d in range(2, dia):
        arreglo[d] = max(montos[d] + arreglo[d - 2], arreglo[d - 1])

    return arreglo[dia], arreglo



def main():
    montos = [100, 20, 30, 70, 20]

    optimos = juan_el_vago_iter(montos, len(montos) - 1)
    print(f'Optimo: {juan_el_vago(montos, len(montos) - 1)}')
    print(f'Optimo: {juan_el_vago_iter(montos, len(montos) - 1)}')
    print(f'Optimo: {juan_el_vago_con_caso_base(montos, len(montos))}')

    solucion = reconstruir_solucion(optimos[1], len(montos) - 1, montos, [])
    solucion.reverse()

    print(f"\nSolucion reconstruccion: {solucion}")



main()