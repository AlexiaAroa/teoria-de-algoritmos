# Pedido grupos -> control de diferentes kilometros de la ruta costera
# Rango de km -> [(NRO, INICIO, FIN), (NRO, INICIO, FIN), ... (NRO, INICIO, FIN)] por cada mafia/grupo
# No pueden solaparse
# Maximizar la cantidad de permisos otorgados
NRO = 0
INICIO = 1
FIN = 2

def mafioso_arnook(pedidos):
    # ordeno de menor a mayor por km fin
    pedidos = sorted(pedidos, key=lambda x: x[FIN])
    solucion = []

    for pedido in pedidos:
        if len(solucion) == 0 or not hay_interseccion(solucion[-1], pedido):
            solucion.append(pedido)

    return solucion

def hay_interseccion(elem_solucion, elem_pedido):
    return elem_pedido[INICIO] < elem_solucion[FIN]

pedidos = [(0, 0, 5), (1, 3, 9), (2, 5, 15), (3, 20, 21)]
print(mafioso_arnook(pedidos))
