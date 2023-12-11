"""En el reino de Gondor ha incrementado enormemente la delincuencia luego de su urbanización. El rey Aragorn no
quiere que todo su esfuerzo en construir calles resulte en vano, por lo que quiere poner guardianes a vigilar las calles por
las noches. El problema es que cuesta mucho dinero entrenar a dichos guardianes, por lo que quiere reducir al mínimo
la cantidad que sean necesarios entrenar. Sabe que cada guardian puede estar vigilando desde una esquina, y desde allí
tener visibilidad hasta cualquier otra esquina directa. Necesita determinar la cantidad mínima de guardianes que son
necesarios para cubrir todas las calles de su reino. Como primera medida, consulta con el oráculo Alumnus Teorius
Algoritmus (es decir, quien lee esta consigna), para determinar si esto es conseguible en corto tiempo (el oráculo le
pregunó algo sobre tiempo polinomial, que Aragorn no entendió y le dijo “si, eso”).
Tenemos que explicarle a Aragorn que este pedido no es realizable (y debe armarse de paciencia, o no buscar el mínimo
exacto), porque el problema de Guardianes de Gondor es, en realidad, un problema NP-Completo (en su versión de
problema de decisión: “¿Se pueden vigilar todas las calles con esta topología con máximo K guardianes?”).

Explicamos por qué no es un problema polinomial -> Explicamos que es un problema NP-Completo

1) Pertenece a NP?
    Si, se puede verificar en tiempo polinomial (dependiendo de la cantidad esquinas):
    Recibo los guardianes y en qué esquina van a estar. Entonces, voy por todas las esquinas, y si alguna de esas
    no está siendo vigilada, entonces no es solución. Caso contrario, si. 

2) Reducir un problema NP Completo a este problema

    "Necesita determinar la cantidad mínima de guardianes que son necesarios para cubrir todas las calles de su reino."
    -> VERTEX COVER (conjunto de vertices que cubren todas las aristas) y es NP Completo

    Mi grafo en Vertex Cover:
    Vertices: las esquinas
    Aristas: conexion de las esquinas directas/las calles

    Reducir Vertex Cover al Problema Gondor
    Tomo los vertices y los convierto en esquinas. Las aristas, las convierto en las calles.

    Llamo al problema de Gondor con esos nuevos datos. Si puede vigilar todas las calles con K guardianes,
    entonces existe un Vertex Cover de tamaño k.

    

Por lo tanto, Problema Gondor es NP Completo

Como no sabemos si P = NP, no es realizable en un tiempo polinomial
"""