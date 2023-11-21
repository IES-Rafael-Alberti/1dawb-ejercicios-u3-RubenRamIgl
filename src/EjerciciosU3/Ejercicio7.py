def pedirAbecedario():
    abecedario=list("abcdefghijklmnopqrstuvwxyz")

    return abecedario

def eliminarPosiciones(abecedario):
    abecedario_modificado=[letra for (indice, letra) in enumerate(abecedario, start=1) if indice%3!=0]

    print(abecedario_modificado)

def main():
    abecedario=pedirAbecedario()

    eliminarPosiciones(abecedario)

if(__name__=="__main__"):
    main()
