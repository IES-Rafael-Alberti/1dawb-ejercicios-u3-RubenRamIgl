def guardarPrecios():
    precios=[50, 75, 46, 22, 80, 65, 8]

    return precios

def mostrarPrecios(precios):
    maximo=max(precios)
    minimo=min(precios)

    print(f"El precio más alto es {maximo} y el precio más bajo es {minimo}")

def main():
    precios=guardarPrecios()

    mostrarPrecios(precios)

if(__name__=="__main__"):
    main()