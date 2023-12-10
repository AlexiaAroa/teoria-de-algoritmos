# si es impar, no hay forma de que haya venido de una multiplicación * 2
# 1 + OPT[n - 1]

# si es par, la forma de llegar es desde una multiplicación * 2, o, de sumar 1
# 1 + OPT[n / 2] 
# 1 + OPT[n - 1]

def cant_operaciones(k):
    optimos = [0] * (k + 1)

    if k == 0:
        return optimos, 0

    for i in range(1, len(optimos)):
        # es impar
        if i % 2 != 0:
            optimos[i] = 1 + optimos[i - 1]
            continue
            
        # si par
        optimos[i] = 1 + min(optimos[i // 2], optimos[i - 1])

    return optimos, optimos[k]

def _reconstruir(optimos, k, solucion):
    if k == 0:
        return solucion
    
    # es impar
    if k % 2 != 0:
        solucion.append("sumar 1")
        return _reconstruir(optimos, k - 1, solucion)
    
    # es par
    if optimos[k // 2] < optimos[k - 1]:
        solucion.append("multiplicar por 2")
        return _reconstruir(optimos, k // 2, solucion)
    
    solucion.append("sumar 1")
    return _reconstruir(optimos, k - 1, solucion)

def reconstruir(optimos, k):
    solucion = _reconstruir(optimos, k , [])
    solucion.reverse()
    return solucion

k = 15
soluciones = cant_operaciones(k)
print(f"Cant operaciones:  {soluciones[1]} | Operaciones: {reconstruir(soluciones[0], k)}")