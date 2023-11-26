def mostrarMenu():
    print("Menú:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

def añadirCliente(baseDatos):
    nif=input("Introduce el NIF del cliente: ")
    nombre=input("Introduce el nombre del cliente: ")
    direccion=input("Introduce la dirección del cliente: ")
    telefono=input("Introduce el teléfono del cliente: ")
    correo=input("Introduce el correo del cliente: ")
    preferente= input("¿Es cliente preferente? (si/no): ").lower()

    cliente={
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "correo": correo,
        "preferente": preferente=="si"
    }

    baseDatos[nif]=cliente
    print(f"Cliente {nombre} añadido correctamente.")

def eliminarCliente(baseDatos):
    nif=input("Introduce el NIF del cliente a eliminar: ")
    if nif in baseDatos:
        cliente_eliminado = baseDatos.pop(nif)
        print(f"Cliente {cliente_eliminado['nombre']} eliminado correctamente")
    else:
        print("Cliente no encontrado en la base de datos.")

def mostrarCliente(baseDatos):
    nif = input("Introduce el NIF del cliente a mostrar: ")
    if nif in baseDatos:
        cliente=baseDatos[nif]
        print("Datos del cliente:")
        print(f"NIF: {nif}")
        for clave, valor in cliente.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print("Cliente no encontrado en la base de datos.")

def listarClientes(baseDatos):
    print("Lista de todos los clientes:")
    for nif, cliente in baseDatos.items():
        print(f"NIF: {nif}, Nombre: {cliente["nombre"]}")

def listarClientesPreferentes(baseDatos):
    print("Lista de clientes preferentes:")
    for nif, cliente in baseDatos.items():
        if cliente["preferente"]:
            print(f"NIF: {nif}, Nombre: {cliente["nombre"]}")

def main():
    baseDatos={}
    salir=False

    while not salir:
        mostrarMenu()
        opcion = input("Selecciona una opción (1-6): ")

        if(opcion=="1"):
            añadirCliente(baseDatos)
        elif(opcion=="2"):
            eliminarCliente(baseDatos)
        elif(opcion=="3"):
            mostrarCliente(baseDatos)
        elif(opcion=="4"):
            listarClientes(baseDatos)
        elif(opcion=="5"):
            listarClientesPreferentes(baseDatos)
        elif(opcion=="6"):
            print("Programa terminado.")
            salir=True
        else:
            print("Opción no válida")

if(__name__=="__main__"):
    main()