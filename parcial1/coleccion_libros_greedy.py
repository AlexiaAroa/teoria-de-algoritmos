# n libros con diferentes espesores de 1 a n (no necesariamente enteros)
# capacidad cajas L (>= n)

def coleccion_libros(libros, capacidad_caja):
    # Ordeno los espesores de mayor a menor
    libros = sorted(libros, reverse=True)
    cajas = []

    for libro in libros:
        if len(cajas) == 0:
            cajas.append(libro)
            continue

        if libro + cajas[-1] <= capacidad_caja:
            cajas[-1] += libro
            continue

        cajas.append(libro)

    return len(cajas)

capacidad_caja = 5
libros = [5, 2, 3, 1, 4]
solucion = coleccion_libros(libros, capacidad_caja)
print(f'Cant cajas: {solucion}')
