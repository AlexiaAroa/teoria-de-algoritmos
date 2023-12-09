def interval_coloring(actividades):
    actividades.sort(key=lambda x: x[1])
    colores = [0] * len(actividades)
    for i in range(len(actividades)):
        for j in range(i):
            if actividades[i][0] >= actividades[j][1]:
                colores[i] = colores[j]
                break
        else:
            colores[i] = max(colores) + 1
            
    return colores