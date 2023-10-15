# Dado unos productos en un arreglo R, donde R[i] nos dice el precio del producto.
# Cada día debemos comprar 1 solo producto, teniendo en cuenta que en todos los días
# los precios aumentan (por ejemplo, el doble).

# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos
# los productos.

def compras_inflacion(productos):
    # Me conviene comprar el producto más caro para que no sea aún más caro en los siguientes días.
    precio_final = 0

    while len(productos) > 0:
        productos = sorted(productos, reverse=True)
        precio_final += productos.pop(0)
        productos = list(map(actualizar_precios, productos))

    return precio_final

def actualizar_precios(precio):
    return precio * 2

def main():
    productos = [40, 60, 20, 70, 80]
    respuesta = compras_inflacion(productos)
    print("Precio minimo para comrpar todos los productos:", respuesta)

main()