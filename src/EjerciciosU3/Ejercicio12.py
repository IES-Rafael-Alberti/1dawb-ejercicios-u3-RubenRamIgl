def matrices():
    matriz_1=((1,2),(3,4),(5,6))
    matriz_2=((-1,0),(0,1),(1,1))

    return matriz_1, matriz_2

def producto(matriz_1, matriz_2):
    matriz_3=[]

    for fila in range(3):
        matriz_3.append([])
        for columna in range(2):
            matriz_3[fila].append(matriz_1[fila][columna]*matriz_2[fila][columna])

    return matriz_3

def main():
    matriz_1, matriz_2=matrices()
    matriz_3=producto(matriz_1, matriz_2)

    for fila in matriz_3:
        print(fila)

    

if(__name__=="__main__"):
    main()