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

def pedirNotas(asignaturas):
    notas=[]
    for asignatura in asignaturas:
        nota=input(f"{asignatura}: ")
        notas.append(nota)
    
    return notas

def mostrarDatos(asignaturas,notas):
    for i in range(len(asignaturas)):
        print(f"En {asignaturas[i]} has sacado un {notas[i]}")

def main():
    asignaturas=pedirAsignaturas()
    notas=pedirNotas(asignaturas)

    mostrarDatos(asignaturas,notas)

if(__name__=="__main__"):
    main()
