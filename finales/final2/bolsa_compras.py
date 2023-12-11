def bolsas_a_usar(peso_maximo, lista_pesos):
    lista_pesos = sorted(lista_pesos, reverse=True)

    bolsas = []
   
    for peso in lista_pesos:
        # si no tengo ninguna bolsa, lo appendeo
        if len(bolsas) == 0:
            bolsas.append(peso)
            continue

        # si ya tengo bolsas, chequeo si entra un producto mas
        if bolsas[len(bolsas) - 1] + peso <= peso_maximo:
            bolsas[len(bolsas) - 1] += peso
            continue

        # si no entra en la bolsa anterior, abro una nueva bolsa
        bolsas.append(peso)
    
    return len(bolsas)