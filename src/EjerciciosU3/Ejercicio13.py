def pedirNumeros():
    numeros=[]
    salir=False
    while not salir:
        numero=int(input("Introduce un número(no introducir nada para salir): "))
        if(numero==""):
            salir=True
        else:
            numeros.append(numero)
    
    return numeros
