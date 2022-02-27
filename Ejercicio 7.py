Algoritmo bandera

constante
    CANTIDAD_FICHAS_MAX : ENTERO ← ???
        # La cantidad max de fichas a ordenar

variable
    fichas : CADENA[COLOR][1,CANTIDAD_FICHAS_MAX]

inicialización
    fichas ← ???

realización
    permutar(fichas, 0, 0, longitud(fichas), longitud(fichas))

fin bandera
