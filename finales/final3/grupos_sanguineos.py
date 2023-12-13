"""Se tiene como posibles grupos sanguíneos de personas O, A, B y AB. Alguien con sangre tipo O sólo puede recibir sangre
tipo O. Alguien de sangre A sólo puede recibir sangre de tipo A u O. Alguien de sangre tipo B sólo puede recibir sangre
de tipo B u O. Alguien con sangre tipo AB puede recibir sangre de cualquier tipo. Se tienen las cantidades de bolsas de
sangre disponibles (SA, SB, SAB, SO) y la cantidad de personas a tratar (PA, PB, PAB, PO). Implementar un algoritmo
greedy que determine cómo se puede satisfacer la demanda de sangre (o si no puede hacerse). Indicar el orden del
algoritmo y justificar por qué el algoritmo propuesto es un algoritmo greedy.

O -> O
A -> A, O
B -> B, O
AB -> cualquier tipo O, A, B, AB

Le damos prioridad a las personas que solo reciban un tipo de sangre.
1) Asignamos O
2) Asignamos los de A -> Inicialmente reciben de tipo A, y si falta, lo completamos con el sobrante de O.
3) Asignamos a los de B -> Inicialmente reciben de tipo B, y si falta, lo completamos con el sobrante de O.
4) Asignamos AB -> Inicialmente reciben de tipo AB. Si falta, se completa con A, B y O

Lo greedy está en el orden en el que planificamos la solución.
"""
A = 0
B = 1
AB = 2
O = 3

def grupos_sanguineos(bolsas, personas):
    if personas[O] > bolsas[O]:
        return False
    
    cant_bolsas_O = bolsas[O] - personas[O]

    if personas[A] > cant_bolsas_O + bolsas[A]:
        return False

    cant_bolsas_A = 0 if bolsas[A] - personas[A] < 0 else bolsas[A] - personas[A]
    cant_bolsas_O -= 0 if bolsas[A] - personas[A] >= 0 else personas[A] - bolsas[A]

    if personas[B] > cant_bolsas_O + bolsas[B]:
        return False

    cant_bolsas_B = 0 if bolsas[B] - personas[B] < 0 else bolsas[B] - personas[B]
    cant_bolsas_O -= 0 if bolsas[B] - personas[B] >= 0 else personas[B] - bolsas[B]

    if personas[AB] > bolsas[AB] + cant_bolsas_B + cant_bolsas_A + cant_bolsas_O:
        return False
    
    return True


print(grupos_sanguineos([10, 10, 10, 10], [9, 5, 15, 8]))
