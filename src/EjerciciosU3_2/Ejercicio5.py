def pedirAsignaturas():
    asignaturas={}
    salir=False

    while not salir:
        asignatura=input("Introduce una asignatura (no introducir nada para salir): ")
        if(asignatura==""):
            salir=True
        else:
            creditos=int(input("Introduce su número de créditos: "))
            asignaturas[asignatura]=creditos

    return asignaturas

def mostrarCreditos(asignaturas):
    totalCreditos=0

    for asignatura, creditos in asignaturas.items():
        print(f"{asignatura} tiene {creditos} créditos")
        totalCreditos+=creditos

    print(f"El número total de créditos del curso es: {totalCreditos}")

def main():
    asignaturas=pedirAsignaturas()
    mostrarCreditos(asignaturas)

if __name__ == "__main__":
    main()
