def crearDiccionario():
    entrada_usuario = input("Introduce las palabras en español e inglés separadas por dos puntos, y cada par separado por comas (ejemplo: perro:dog,gato:cat): ")
    
    pares=entrada_usuario.split(",")
    diccionario={}

    for par in pares:
        palabra, traduccion=par.split(":")
        diccionario[palabra]=traduccion

    return diccionario

def traducirFrase(diccionario, frase):
    palabras=frase.split()
    traduccion=[]

    for palabra in palabras:
        traduccion.append(diccionario.get(palabra, palabra))

    return " ".join(traduccion)

def main():
    diccionario=crearDiccionario()

    fraseEspanol=input("Introduce una frase en español: ")
    fraseTraducida=traducirFrase(diccionario, fraseEspanol)

    print("Frase traducida: ", fraseTraducida)

if(__name__=="__main__"):
    main()
