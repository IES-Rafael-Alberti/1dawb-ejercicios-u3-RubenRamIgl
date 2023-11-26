def funcionLetras():
    alfabeto=set("abcdefghijklmnopqrstuvwxyz")
    vocales={"a", "e", "i", "o", "u"}

    consonantes=alfabeto-vocales

    letras_comunes=vocales.intersection(consonantes)

    print("Conjunto de consonantes:", consonantes)
    print("Conjunto de letras comunes:", letras_comunes)

def main():
    funcionLetras()

if(__name__=="__main__"):
    main()
