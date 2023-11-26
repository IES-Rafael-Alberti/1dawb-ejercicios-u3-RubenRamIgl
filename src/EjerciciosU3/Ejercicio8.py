def pedirPalabra():
    palabra=input("Introduce una palabra: ")

    return palabra

def esPalindromo(palabra):

    return palabra==palabra[::-1]

def main():
    palabra=pedirPalabra()

    if(esPalindromo(palabra)):
        print("La palabra es un palíndromo")
    else:
        print("La palabra no es un palíndromo")

if(__name__=="__main__"):
    main()