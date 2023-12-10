# ¿El problema del ejercicio 2 se encuentra en NP? ¿Qué problema NP-Completo visto en la cursada es semejante al
# indicado al del problema del ejercicio 2? ¿qué reducción podríamos hacer? ¿podemos concluir que el problema del
# ejercicio 2 es un problema NP-Completo?


# Si, se encuentra en NP (problema de decision): si me dan los submarinos y los faros yo puedo ver si estan todos iluminados de
# forma rapida, recorriendo la matriz y viendo algunas posiciones en tiempo constante. Esto es proporcional
# al tamaño de la matriz, que es polinomial. -> Tiene un verificador polinomial.

# Problema NP-Completo: Set Cover
# Tengo un conjunto U de submarinos
# y tengo subsets con las posiciones de cada faro -> indican los submarinos que iluminan
# Si la union de esos subsets es igual a U -> esos faros iluminan a todos los submarinos

# Problema de optimización: tomar la menor cantidad de subsets que cubren U
# Problema de decisión: ¿existe una cantidad de subsets <= a K que cubra todo U?
 
# Esto es una Reduccion de Problema de Submarinos a Set Cover

# No nos dice nada sobre si el Problema de los Submarinos es NP-Completo o no.
