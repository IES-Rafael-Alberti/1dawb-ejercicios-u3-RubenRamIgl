def obtenerNombres():
    nombresPrimaria=set()
    nombresSecundaria=set()
    salir=False

    print("Introduce los nombres de los alumnos de primaria (mo introducir nada para finalizar):")
    while not salir:
        nombrePrimaria=input("Introduce el nombre del alumno: ")
        if(nombrePrimaria==""):
            salir=True
        nombresPrimaria.add(nombrePrimaria)

    salir2=False

    print("Introduce los nombres de los alumnos de secundaria (no introducir nada para finalizar):")
    while not salir2:
        nombreSecundaria=input("Introduce el nombre del alumno: ")
        if(nombreSecundaria==""):
            salir2=True
        nombresSecundaria.add(nombreSecundaria)

    return nombresPrimaria, nombresSecundaria

def mostrarResultados(nombresPrimaria, nombresSecundaria):
    print("Nombres de todos los alumnos sin repeticiones:")
    nombreAlumnos=nombresPrimaria.union(nombresSecundaria)
    print(nombreAlumnos)

    print("Nombres que se repiten entre los alumnos de primaria y secundaria:")
    nombresRepetidos=nombresPrimaria.intersection(nombresSecundaria)
    print(nombresRepetidos)

    print("Nombres de primaria que no se repiten en secundaria:")
    nombresNoRepetidos=nombresPrimaria.difference(nombresSecundaria)
    print(nombresNoRepetidos)

    print("¿Todos los nombres de primaria están incluidos en secundaria?")
    todosIncluidos=nombresPrimaria.issubset(nombresSecundaria)
    print(todosIncluidos)

def main():
    nombresPrimaria, nombresSecundaria=obtenerNombres()
    mostrarResultados(nombresPrimaria, nombresSecundaria)

if(__name__=="__main__"):
    main()
