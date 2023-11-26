def datosClientes(listaCompras: list) -> set:
    domicilios=set()

    for compra in listaCompras:
        domicilios.add(compra[3])

    return domicilios

def main():
    listaCompras=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
                  ("Jorge Russo", 7, 699, "Mirasol 218"),
                  ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
                  ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
                  ("Jorge Russo", 15, 958, "Mirasol 218")]

    domiciliosClientes=datosClientes(listaCompras)

    print("Domicilios a los que se debe enviar una factura:")
    for domicilio in domiciliosClientes:
        print(domicilio)

if(__name__=="__main__"):
    main()


