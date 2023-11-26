def preguntarDivisa():
    divisas={"Euro":"€", "Dollar":"$", "Yen":"¥"}

    divisa=input("Introduce el nombre de una divisa: ").title()

    simbolo=mostrarSimbolo(divisas,divisa)

    print(simbolo)
    


def mostrarSimbolo(divisas, divisa):
    return divisas.get(divisa,"No existe la divisa en el diccionario")


def main():
    preguntarDivisa()

if(__name__=="__main__"):
    main()