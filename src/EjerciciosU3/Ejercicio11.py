def vectores():
    v1=[1,2,3]
    v2=[-1,0,2]

    return v1, v2

def productoEscalar(v1,v2):
    resultado=sum(x*y for x, y in zip(v1, v2))

    return resultado

def main():
    v1, v2=vectores()
    producto_escalar=productoEscalar(v1,v2)

    print(f"El producto escalar de v1={v1} y v2={v2} es {producto_escalar}")

if(__name__=="__main__"):
    main()