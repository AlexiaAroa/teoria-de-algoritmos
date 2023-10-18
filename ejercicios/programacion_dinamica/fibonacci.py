# Version 1:
# Complejidad temporal: exponencial
# Complejidad espacial: lineal
def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

# Version 2
# Aplico memoization -> guardo resultados en un arreglo
# Top down
def fibonacci_memo(n):
    FIB = [None] * (n + 1)
    return _fibonacci_memo(n, FIB)

def _fibonacci_memo(n, FIB):
    if n <= 1:
        return n
    
    if FIB[n - 1] == None:
        FIB[n - 1] = _fibonacci_memo(n - 1, FIB)
    if FIB[n - 2] == None:
        FIB[n - 2] = _fibonacci_memo(n - 2, FIB)

    FIB[n] = FIB[n - 1] + FIB[n - 2]
    return FIB[n]

# Version 3
# Aplico memoization -> guardo resultados en un arreglo
# Bottom up

def fibonacci_memo_iterativo(n):
    FIB = [None] * (n + 1)
    return _fibonacci_memo_iterativo(n, FIB)

def _fibonacci_memo_iterativo(n, FIB):
    if n == 0:
        return n
    
    FIB[0] = 0
    FIB[1] = 1

    for i in range(2, len(FIB)):
        FIB[i] = FIB[i - 1] + FIB[i - 2]

    return FIB[n]

# Version 3
# Aplico memoization -> guardo resultados en un arreglo
# Optimización en memoria -> solo necesito los últimos dos valores
# Bottom up
# Complejidad temporal: O(n)
# Complejidad espacial: O(1)

def fibonacci_opt(n):
    if n <= 1:
        return n
    
    actual = 1
    anterior = 0

    for _ in range(1, n):
        siguiente = actual + anterior
        anterior = actual
        actual = siguiente

    return actual
