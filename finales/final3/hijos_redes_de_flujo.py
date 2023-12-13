"""
Carlos tiene un problema: sus 5 hijos no se soportan. Esto es a tal punto, que ni siquiera están dispuestos a caminar
juntos para ir a la escuela. Incluso más: ¡tampoco quieren pasar por una cuadra por la que haya pasado alguno de sus
hermanos! Sólo aceptan pasar por las esquinas, si es que algún otro pasó por allí. Por suerte, tanto la casa como la
escuela quedan en esquinas, pero no está seguro si es posible enviar a sus 5 hijos a la misma escuela. Utilizando lo visto
en la materia, formular este problema y resolverlo. Indicar y justificar la complejidad del algoritmo.

Buscar Disjoint Paths y veo que la cantidad de caminos sea mayor igual a la cantidad de hijos.

Creacion del grafo dirigido para aplicar FF:
Fuente: Casa
Sumidero: Escuela
Vértices: esquinas
Aristas: Representan las calles. Todos pesos 1, siendo esta mi posibilidad de elección/restriccion de que solo se puede usar el camino una vez, 
justamente porque los hijos no pueden ir por un mismo camino. 

Al aplicar FF a este grafo (obtiene los caminos utilizando BFS), se maximiza el flujo de la red, y como el flujo representa los caminos, entonces
maximiza la cantidad de caminos en base a mis restricciones.
Por lo tanto, si el flujo maximo, siendo este la cantidad caminos distintos, es mayor o igual 5, si es posible mandar a 
todos los hijos a la misma escuela, caso contrario, no.

La complejidad del algoritmo es O(V*E)
Por tener las aristas en 1...
"""