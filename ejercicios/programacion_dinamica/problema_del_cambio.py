# C[cambio] = 1 + min (para toda moneda del sistema <= cambio: C[cambio - moneda])

def problema_del_cambio(sistema, cambio_pedido):
    C = [0] * (cambio_pedido + 1)

    for cambio_actual in range(1, cambio_pedido + 1):
        minimo = cambio_actual # como minimo tomo todas las monedas de 1

        for moneda in sistema:
            if moneda <= cambio_actual:
                actual = 1 + C[cambio_actual - moneda]
                if actual < minimo:
                    minimo = actual

        C[cambio_actual] = minimo

    return C[cambio_pedido]

sistema = [1, 5, 6, 9]
cambio = 11
respuesta = problema_del_cambio(sistema, cambio)
print("Cant de monedas: ", respuesta)