def numeros():
    numeros={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    pares=set()
    for num in numeros:
        if(num%2==0):
            pares.add(num)

    multiplos_de_tres=set()
    for num in numeros:
        if(num%3==0):
            multiplos_de_tres.add(num)

    pares_y_multiplos_de_tres=set()
    for num in pares:
        if(num in multiplos_de_tres):
            pares_y_multiplos_de_tres.add(num)

    return pares, multiplos_de_tres, pares_y_multiplos_de_tres

def imprimirResultados(pares, multiplos_de_tres, pares_y_multiplos_de_tres):
    print("Conjunto de números pares:", pares)
    print("Conjunto de números múltiplos de tres:", multiplos_de_tres)
    print("Intersección entre pares y múltiplos de tres:", pares_y_multiplos_de_tres)

def main():
    pares, multiplos_de_tres, pares_y_multiplos_de_tres=numeros()

    imprimirResultados(pares, multiplos_de_tres, pares_y_multiplos_de_tres)

if(__name__=="__main__"):
    main()