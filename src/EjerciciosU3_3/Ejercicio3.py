def conjunto_potencia(s):
    listaS=list(s)
    n=len(listaS)

    potencia=[]
    for i in range(2**n):
        subset=set()
        for j in range(n):
            if((i//(2**j))%2==1):
                subset.add(listaS[j])
        potencia.append(subset)

    return potencia

def main():
    conjunto={6, 1, 4}
    resultado=conjunto_potencia(conjunto)

    print(f"Conjunto potencia de {conjunto}:")
    for subset in resultado:
        print(subset)

if(__name__=="__main__"):
    main()
