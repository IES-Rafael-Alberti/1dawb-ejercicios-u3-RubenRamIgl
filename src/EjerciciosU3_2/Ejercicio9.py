def mostrarEstado(cobrado, pendiente):
    print(f"\nCantidad cobrada hasta el momento: {cobrado}")
    print(f"Cantidad pendiente de cobro: {pendiente}\n")

def gestionarFacturas():
    facturas={}
    cobrado=0
    salir=False

    while not salir:
        print("1. Añadir nueva factura")
        print("2. Pagar factura existente")
        print("3. Terminar")

        opcion=input("Seleccione una opción (1/2/3): ")

        if(opcion=="1"):
            numeroFactura=input("Introduzca el número de factura: ")
            coste=float(input("Introduzca el coste de la factura: "))
            facturas[numeroFactura]=coste
            cobrado+=coste
            mostrarEstado(cobrado, sum(facturas.values()))
        elif(opcion=="2"):
            if not facturas:
                print("No hay facturas pendientes de pago")
            else:
                numeroFactura=input("Introduzca el número de factura a pagar: ")
                if(numeroFactura in facturas):
                    cobrado+=facturas.pop(numeroFactura)
                    mostrarEstado(cobrado, sum(facturas.values()))
                else:
                    print("La factura no existe.")
        elif(opcion=="3"):
            salir=True
        else:
            print("Opción no válida")

def main():
    gestionarFacturas()

if(__name__=="__main__"):
    main()
