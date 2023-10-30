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

def main():
    montos = [100, 20, 30, 70, 20]

    print(f'Optimo: {juan_el_vago(montos, len(montos) - 1)}')
    print(f'Optimo: {juan_el_vago_iter(montos, len(montos) - 1)}')


main()