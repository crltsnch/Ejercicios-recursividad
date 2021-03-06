Algoritmo bandera

CONSTANTES
    TECLADO, PANTALLA : NOMBRE_INTERNO
        # Archivos consola de nombres definidos por le SAA
    SEPARADOR : CADENA ← ’ — ’
        # Separa la cadena inicial de la cadena ordenada
    NUEVA_LINEA : CADENA ← cadena(código(13))
        # Retorno carro
    NOMBRE_FICHAS_MAX : ENTERO ← ???
        # La cantidad max de fichas max a ordenar

VARIABLES
    fichas : CADENA[COLOR][1,CANTIDAD_FICHAS_MAX]

PRECONDICION
    índice_válido(serie_fichas, 1)
    índice_válido(serie_fichas, n)

    sub_cadena(serie_fichas, 1, n) ≠ NULO
    0 ≤ i ≤ n 
    0 ≤ j ≤ n
    0 ≤ k ≤ n
    (∀m ∈ ℕ)
           (  1 ≤ m ≤ i => ítem(serie_fichas, m) = 'R')
           (i+1 ≤ m ≤ j => ítem(serie_fichas, m) = 'V')
           (k+1 ≤ m ≤ n => ítem(serie_fichas, m) = 'B')

REALIZACION
    permutar(serie_fichas : CADENA ; i, j, k, n : ENTERO)
    si k ≠ j entonces
        # Falta desplazar fichas de índices comprendidos entre 
        # j+1 y k. Observar la fiche de índice j+1
        según el valor de
            ítem(serie_fichas, j+1)
        hacer
            si 'R' entonces
                # La ficha es Roja: intercambiarla con la ficha
                # Verde que ocupa el lugar i+1
                intercambiar(
                          ítem(serie_fichas, i+1),
                          ítem(serie_fichas, j+1)
                        )
                # (A1') : Rojas desde 1 hasta i+1
                # (A2') : Verdes desde i+2 hasta j+1
                # (A3 ) : Azules desde k+1 hasta n
                permutar(serie_fichas, i+1, j+1, k, n)
            fin si

            si 'V' entonces
                # La ficha es Verde: está en su lugar y S2
                # se extiende desde i+1 hasta j+1
                # (A1 ) : Rojas desde 1 hasta i
                # (A2') : Verdes desde i+1 hasta j+1
                # (A3 ) : Azules desde k+1 hasta n
                permutar(serie_fichas, i, j+1, k, n)
            fin si

            si 'B' entonces
                # La ficha es Azul: intercambiarla con la ficha
                # de índice k
                intercambiar(
                          ítem(serie_fichas, j+1),
                          ítem(serie_fichas, k)
                        )
                # (A1 ) : Rojas desde 1 hasta i
                # (A2 ) : Verdes desde i+1 hasta j
                # (A3') : Azules desde k hasta n
                permutar(serie_fichas, i, j, k-1, n)
            fin si
        fin hacer
    fin si

POSTCONDICION
    antiguo(i) = i ; antiguo(j) = j ; antiguo(k) = k
    serie_fichas = 'RR..RVV..VBB..B'
fin permutar


fin bandera
