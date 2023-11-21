def almacenarNumeros():
    numeros=[]

    for i in range(1, 11):
        numeros.append(i)

    numeros.reverse()
    return numeros

def imprimirNumeros(numeros):
    print(numeros)

def main():
    numeros = almacenarNumeros()
    imprimirNumeros(numeros)

if __name__ == "__main__":
    main()
