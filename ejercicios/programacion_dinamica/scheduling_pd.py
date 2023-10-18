# Tengo un aula donde quiero dar charlas. Las charlas tinen un horario
# de inicio y fin, y un peso asociado al valor de cada charla.
# Quiero utilizar el aula para maximizar la sumatoria de pesos de las charlas dadas.

INICIO = 0
FIN = 1
VALOR = 2

# Caso base: no tengo charlas, ganancia 0

# Charla n, tengo dos opciones, dar la charla o no darla.

# Ecuación de recurrencia
# OPT(charla_i) = max(OPT(charla_(i-1)), ganancia_i + OPT(charla[p[i]]))

# Primero, ordenamos por horario de fin


# TERMINAR
def scheduling_con_pesos(charlas):
    if len(charlas) == 0:
        return 0
    
    charlas = ordenar_por_horario_de_fin(charlas)

def calcular_arreglo_de_no_intersecciones(charlas):
    P = [0] * len(charlas)
    for i in range(len(charlas)):
        P[i] = _calcular_arreglo_de_no_intersecciones(charlas, i, len(charlas) - 1)

def _calcular_arreglo_de_no_intersecciones(charlas, inicio, fin):
    if inicio > fin:
        return 0
    
    medio = (inicio + fin) / 2
    if not hay_interseccion(charlas[medio], charlas[medio + 1]) and hay_interseccion(charlas[medio], charlas[medio + 1]):
        return medio
    
    if hay_interseccion(charlas[medio], charlas[medio + 1]) and hay_interseccion(charlas[medio], charlas[medio + 1]):
        return _calcular_arreglo_de_no_intersecciones(charlas, inicio, medio - 1)
    
    return _calcular_arreglo_de_no_intersecciones(charlas, medio + 1, fin)

def hay_interseccion(charla_1, charla_2):
    return charla_2[INICIO] < charla_1[FIN]

def ordenar_por_horario_de_fin(charlas):
    return sorted(charlas, key=lambda charla: charla[FIN])