# Escribir un algoritmo de tipo Backtracking que reciba una cantidad de dados n y una suma s.
# La función debe devolver todas las tiradas posibles de n dados cuya suma es s.
# Por ejemplo, con n = 2 y s = 7, debe devolver [1, 6] [2, 5] [3, 4] [4, 3] [5, 2] [6, 1].
# ¿De qué orden es el algoritmo en tiempo? ¿Y en memoria?

VALORES_DADO = [1, 2, 3, 4, 5, 6]

def suma_dados(cantidad_dados, suma, i_act, solucion, solucion_parcial):
    if len(solucion_parcial) == cantidad_dados and sum(solucion_parcial) == suma:
        solucion.append(solucion_parcial[:])
        return
    
    if len(solucion_parcial) == cantidad_dados and sum(solucion_parcial) != suma:
        return
    
    if i_act == len(VALORES_DADO):
        return
    
    valor_actual = VALORES_DADO[i_act]
    solucion_parcial.append(valor_actual)
    suma_dados(cantidad_dados, suma, i_act + 1, solucion, solucion_parcial)
    solucion_parcial.remove(valor_actual)
    suma_dados(cantidad_dados, suma, i_act + 1, solucion, solucion_parcial)



def suma_dados_v2(cantidad_dados, suma, solucion, solucion_parcial):
    if len(solucion_parcial) == cantidad_dados and sum(solucion_parcial) == suma:
        solucion.append(solucion_parcial[:])
        return

    if len(solucion_parcial) == cantidad_dados and sum(solucion_parcial) != suma:
        return

    for i in range(1, 7):
        solucion_parcial.append(i)
        suma_dados_v2(cantidad_dados, suma, solucion, solucion_parcial)
        solucion_parcial.remove(i)
  

n = 2
s = 7
solucion = []
suma_dados(n, s, 0, solucion, [])
print(solucion) # Solo lo toma en una direccion

solucion2 = []
suma_dados_v2(n, s, solucion2, [])
print(solucion2) # Aca si estan todas las combinaciones

