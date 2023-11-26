def crearDiccionario():
    diccionario={"Plátano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}

    return diccionario

def pedirDatos(diccionario):
    salir=False

    while not salir:
        fruta=input("Introduce una fruta(no introducir nada para salir): ").title()
        kilos=float(input("Introduce los kilos: "))
        if(fruta==""):
            salir=True
        try:
            if fruta in diccionario:
                precio=diccionario[fruta]*kilos
                print(f"El precio de {kilos} kilos de {fruta} es: {precio}")
            else:
                print("La fruta no está en el diccionario")
        except ValueError:
            print("Error, introduce un número de kilos válido")

def main():
    diccionario=crearDiccionario()

    pedirDatos(diccionario)

if(__name__=="__main__"):
    main()

