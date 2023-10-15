# Tengo un aula donde quiero dar charlas. Las charlas tienen horario de
# inicio y fin. Quiero utilizar el aula para dar la mayor cantidad de charlas.

# Cada charla tiene un horario de inicio, horario de fin.
INICIO = 0
FIN = 1

def scheduling(charlas):
    # Ordenamos las charlas por horario de fin
    # De esta forma, tomo la charla que termine primero para liberar el aula
    # lo más rápido posible y dar lugar al resto de las charlas.
    # Regla sencilla: me tengo que asegurar que la charla que tome, no colisione con la 
    # última que ya agregué

    # No hay forma de que haya otra charla que sea mejor que esa, porque
    # esa otra charla terminaría después -> lo cual colisiona con otras charlas

    # No importa cuándo comience la charla, lo importante es que termine lo más antes posible

    charlas_ordenadas = sorted(charlas, key=lambda horario: horario[FIN])
    charlas_respuesta = []

    for charla in charlas_ordenadas:
        if len(charlas_respuesta) == 0 or not hay_interseccion(charlas_respuesta[-1], charla):
            charlas_respuesta.append(charla)

    return charlas_respuesta

def hay_interseccion(charla_1, charla_2):
    return charla_2[INICIO] < charla_1[FIN]

def main():
    charlas = [(10, 12), (11, 15), (14, 17), (17, 21), (16, 20), (9, 22)]
    respuesta = scheduling(charlas)
    print("Charlas a realizar:", respuesta)

main()

