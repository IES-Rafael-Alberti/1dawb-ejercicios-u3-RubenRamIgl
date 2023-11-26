def pedirDatos():
    diccionario={}
    salir=False

    while not salir:
        nombre=input("Nombre: ")
        edad=input("Edad: ")
        sexo=input("Sexo: ")
        telefono=input("Teléfono: ")
        correo=input("Correo electrónico: ")

        diccionario["Nombre"]=nombre
        diccionario["Edad"]=edad
        diccionario["Sexo"]=sexo
        diccionario["Teléfono"]=telefono
        diccionario["Correo electrónico"]=correo

        print("Contenido del diccionario:")
        for clave, valor in diccionario.items():
            print(f"{clave}: {valor}")

        salir=True

def main():
    pedirDatos()

if(__name__=="__main__"):
    main()