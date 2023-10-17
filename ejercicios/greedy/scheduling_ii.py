# Minimizando latencia maxima
DURACION = 0
DEADLINE = 1

# Ordenamos por deadline de menor a mayor:
# Se realizan las tareas que terminan antes: hacemos que los trabajos que 
# se necesiten terminar primero, se hagan primero.

def minimizar_latencia_maxima(tareas):
    tareas = sorted(tareas, key=lambda tarea: tarea[DEADLINE])
    inicio = 0
    latencia = 0

    for tarea in tareas:
        finalizacion = inicio + tarea[DURACION]
        if finalizacion - tarea[DEADLINE] > latencia:
            latencia = finalizacion - tarea[DEADLINE]
        
        inicio = finalizacion

    return latencia

def main():
    # (DURACION, DEADLINE)
    tareas = [(1, 2), (10, 10)]
    latencia_maxima = minimizar_latencia_maxima(tareas)
    print(latencia_maxima)

main()