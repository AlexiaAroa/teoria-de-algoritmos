# Implementar un algoritmo que devuelva el cambio pedido,
# usando la mínima cantidad de billetes.

# Ordenamos los billetes de mayor a menor denominación.
# Si el cambio es mas grande o igual que el billete de mayor denominación, tomo el billete y se lo resto al cambio.
# Repito hasta que el cambio sea menor a el valor de ese billete, y continúo con el siguiente.
# Si el cambio es mas chico, pruebo con el siguiente billete.

# No funciona con todos los sistemas monetarios
# Si mi sistema es [9, 6, 5, 1] y el cambio es de 11
# Mi algoritmo retorna 1 billete de 9, y 2 billetes de 1 (total 3 billetes)
# cuando una solución óptima es 1 billete de 6 y un billete de 5 (total 2 billetes)

def problema_del_cambio(billetes, cambio_pedido):
    billetes = sorted(billetes, reverse=True)
    resultado = {}

    for billete in billetes:
        while cambio_pedido >= billete:
            resultado[billete] = resultado.get(billete, 0) + 1
            cambio_pedido -= billete

    return resultado

def main():
    sistema_monetario = [5, 10, 50, 20, 100, 1]
    cambio_pedido = 90

    resultado = problema_del_cambio(sistema_monetario, cambio_pedido)

    for billete, cantidad in resultado.items():
        print("Billete:", billete, "Cantidad:", cantidad)

main()
