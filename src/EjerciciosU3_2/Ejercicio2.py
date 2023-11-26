def pedirDatos():
    salir=False
    while not salir:
        try:
            nombre=input("Introduce tu nombre: ")
            edad=input("Introduce tu edad: ")
            direccion=input("Introduce tu direccion: ")
            telefono=input("Introduce tu telefono: ")
            if(int(edad)<0):
                raise ValueError
            salir=True
        except ValueError:
            print("edad no válida")

    return nombre, edad, direccion, telefono

def mostrarDiccionario(nombre, edad, direccion, telefono):
    diccionario={"Nombre":nombre,"Edad":edad, "Dirección":direccion, "Teléfono":telefono}

    print(f"{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {telefono}.")

def main():
    nombre, edad, direccion, telefono=pedirDatos()

    mostrarDiccionario(nombre, edad, direccion, telefono)

if(__name__=="__main__"):
    main()

        