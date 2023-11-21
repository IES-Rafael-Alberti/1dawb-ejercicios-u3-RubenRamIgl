def pedirAsignaturas():
    asignaturas=[]
    salir=False
    while not salir:
        asignatura=input("Introduce una asignatura(no introducir nada para salir): ")
        if(asignatura==""):
            salir=True
        else:
            asignaturas.append(asignatura)
    
    return asignaturas

def imprimirDatos(asignaturas):
    for i in asignaturas:
            print("Yo estudio "+i)

def main():
    asignaturas=pedirAsignaturas()

    imprimirDatos(asignaturas)

if(__name__=="__main__"):
    main()