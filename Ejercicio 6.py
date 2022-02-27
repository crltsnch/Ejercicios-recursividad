#Ejercicio 6: Reconocer un palíndromo
Programa palíndromo


# Esperar la escritura en teclado de la primera frase a analizar
leer(TECLADO)
frase ← copia_buffer(TECLADO)

hasta que frase = CADENA_VACIA repetir
    # Analizar la frase introducida y mostrar la respuesta
    escribir(PANTALLA, frase)

    si
        palindromo(frase)
    entonces
        escribir(PANTALLA, ’ es un palíndromo.')
    si no
        escribir(PANTALLA, / no es un palíndromo./)
    fin si

    # Esperar la escritura en teclado de frase siguiente a analizar
    leer(TECLADO)
    frase ← copia_buffer(TECLADO)

fin repetir

fin programa palindromo
