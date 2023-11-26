def pedirNumeros():
    numeros=[]
    salir=False
    while not salir:
        n=input("Introduce un número(no introducir nada para salir): ")
        if(str(n)==""):
            salir=True
        else:
            numeros.append(int(n))

    numeros.sort()
    return numeros

def imprimirNumeros(numeros):
    print(numeros)

def main():
    numeros=pedirNumeros()

    imprimirNumeros(numeros)

if(__name__=="__main__"):
    main()