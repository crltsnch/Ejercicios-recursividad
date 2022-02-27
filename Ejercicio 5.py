#Ejercicio resuelto 5: Búsqueda recursiva por dicotomía en una tabla ordenada
Algoritmo dicotomía

ENTRADA
    tabla:TABLA[T -> COMPARABLE]
    t:T

Resultado:ENTERO


PRECONDICION
    t ≠ NULO
    tabla ≠ NULO

    está_ordenada_asc(tabla) #tabla ordenada ascendentemente

    tabla[índice_min(tabla)] ≤ t ≤ tabla[índice_max(tabla)] #t dentro de la tabla
