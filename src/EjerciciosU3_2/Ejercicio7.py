def crearCesta():
    cesta={}
    salir=False

    while not salir:
        articulo=input("Introduce un artículo (no introducir nada para terminar)): ")
        if articulo=="":
            salir=True
        else:
            precio=float(input("Introduce su precio: "))
            cesta[articulo]=precio

    return cesta

def mostrarCesta(cesta):
    print("Lista de la compra:")
    total=0
    for articulo, precio in cesta.items():
        print(f"{articulo}: {precio} euros")
        total+=precio
    print(f"Coste total: {total} euros")

def main():
    cestaCompra=crearCesta()
    mostrarCesta(cestaCompra)

if(__name__=="__main__"):
    main()
