
""" Suponiendo que como minimo voy a tener 2 bifurcaciones
    bifurcaciones es un arreglo con tuplas (ciudad: string, km: entero)
    -> Lo hice directamente como si fuera un arreglo de enteros.
    
    El patrullero cubre 50 km hacia adelante y hacia atras
    
    Ordenamos por km de menor a mayor
    
    Tengo 2 procesos
    El primero es que si supera los 50km de la ciudad aux entonces agrego el policia en la ciudad anterior.
    El segundo es ignorar todas las ciudad que son cubiertas por este ultimo policia agregado, hasta
    llegar a uno que no lo cubra. Actualizo mi ciudad aux con esta ciudad no cubierta y
    vuelvo al primer proceso.
   
    Casos extra:
    Si estoy en el ultimo elemento y no agregue ninguna patrulla (porque estaban muy cerca las ciudades)
    o la ultima patrulla agregada no cubre esta ultima ciudad, entonces agrego
    una patrulla en esta ultima ciudad.
 
"""
CIUDAD = 0
KM = 1

def ejercicio_1(bifurcaciones):
    patrullas = []
    b_ordenadas = sorted(bifurcaciones) # Suponiendo O(n log n)
    patrulla_aux = b_ordenadas[0]
    km_cubiertos = 0 # La uso una vez que agrego el patrullero
    
    for i in range(1, len(b_ordenadas)): # O(n)
        # Primer proceso
        if b_ordenadas[i] > patrulla_aux + 50 and not km_cubiertos: # Es como si estuviera chequeando del patrullero hacia la izq
            patrullas.append(b_ordenadas[i-1])
            km_cubiertos = b_ordenadas[i-1] + 50 # lo posiciono en donde agregue la patrulla y le sumo 50 que es todo lo que cubre

        # Segundo Proceso
        if km_cubiertos and b_ordenadas[i] > km_cubiertos: # Es como si estuviera chequeando del patrullero hacia la der
            patrulla_aux = b_ordenadas[i]
            km_cubiertos = 0
        
        # Si no agregue ninguna patrulla porque estaban muy cerca o en el ultimo caso tambien estaban muy cerca
        if i == len(b_ordenadas) - 1 and (len(patrullas) == 0 or patrullas[-1] + 50 < b_ordenadas[i]):
            patrullas.append(b_ordenadas[i])

    return patrullas
    

def main():
    patrullas = [156, 194, 185, 270, 249]
    res1 = ejercicio_1(patrullas)
    print(res1) 
  
    patrullas_2 = [156, 194, 185, 270, 249, 213]
    res2 = ejercicio_1(patrullas_2)
    print(res2)
    
    patrullas_cercanas = [100, 123, 115, 113, 134, 141]
    res3 = ejercicio_1(patrullas_cercanas)
    print(res3)

main()
