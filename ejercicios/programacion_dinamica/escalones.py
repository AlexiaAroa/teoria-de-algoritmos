# Problema de los 2 escalones
# Tenemos la capacidad de subir escalones de a 1 o 2 pasos.

# Caso base -> 0 escalones: 1 forma de subir
# Si tengo 1 escalon: 1 forma de subir
# Si tengo 2 escalones: tengo 2 formas de subir (dar dos pasos simples o un paso doble)
# Ecuacion de recurrencia: T(n) = T(n-1) + T(n-2) (Fibanocci)

# escalera: cantidad de escalones
def escalones(cant_escalones):
    if cant_escalones <= 2:
        return cant_escalones
    
    return escalones(cant_escalones - 1) + escalones(cant_escalones - 2)

def escalones_v2(cant_escalones):
    if cant_escalones <= 1:
        return 1
    
    if cant_escalones == 2:
        return 2
    
    actual = 2
    anterior = 1

    for _ in range(2, cant_escalones):
        siguiente = actual + anterior
        anterior = actual
        actual = siguiente

    return actual


# Problema de los 3 escalones
# Tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos.
# Caso base -> 0 escalones: 1 forma de subir
# Si tengo 1 escalon: 1 forma de subir
# Si tengo 2 escalones: tengo 2 formas de subir (dar dos pasos simples o un paso doble)
# Si tengo 3 escalones: tengo 4 formas de subir (dar tres pasos simples, un paso doble + uno simple, uno simple + uno doble, un paso triple)

def problema_3_escalones(cant_escalones):
    if cant_escalones <= 1:
        return 1
    
    if cant_escalones == 2:
        return 2
    
    if cant_escalones == 3:
        return 4
    
    return problema_3_escalones(cant_escalones - 1) + problema_3_escalones(cant_escalones - 2) + problema_3_escalones(cant_escalones - 3)


def problema_3_escalones_v2(cant_escalones):
    if cant_escalones <= 1:
        return 1
    
    if cant_escalones == 2:
        return 2
    
    if cant_escalones == 3:
        return 4
    

    actual = 4
    anterior = 2
    anterior_2 = 1

    for _ in range(3, cant_escalones):
        siguiente = actual + anterior + anterior_2
        anterior_2 = anterior
        anterior = actual
        actual = siguiente

    return actual

def main():
    print("DE A 1 O 2 PASOS")
    print(f'3 escalones: {escalones_v2(3)} formas')
    print(f'4 escalones: {escalones_v2(4)} formas')
    print(f'5 escalones: {escalones_v2(5)} formas')

    print("\nDE A 1 O 2 O 3 PASOS - recursivo")
    print(f'3 escalones: {problema_3_escalones(3)} formas')
    print(f'4 escalones: {problema_3_escalones(4)} formas')
    print(f'5 escalones: {problema_3_escalones(5)} formas')

    print("\nDE A 1 O 2 O 3 PASOS - iterativo memo")
    print(f'3 escalones: {problema_3_escalones_v2(3)} formas')
    print(f'4 escalones: {problema_3_escalones_v2(4)} formas')
    print(f'5 escalones: {problema_3_escalones_v2(5)} formas')

main()