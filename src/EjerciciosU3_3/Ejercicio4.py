def funcionFrutas(frutas1, frutas2):
    set_frutas1, set_frutas2=set(frutas1), set(frutas2)
    frutas_comunes=set_frutas1 & set_frutas2
    frutas_solo_en_frutas1=set_frutas1-set_frutas2
    frutas_solo_en_frutas2=set_frutas2-set_frutas1
    return frutas_comunes, frutas_solo_en_frutas1, frutas_solo_en_frutas2

def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    frutas_comunes, frutas_solo_en_frutas1, frutas_solo_en_frutas2=funcionFrutas(frutas1, frutas2)

    print("Conjunto de frutas comunes:", frutas_comunes)
    print("Conjunto de frutas solo en frutas1:", frutas_solo_en_frutas1)
    print("Conjunto de frutas solo en frutas2:", frutas_solo_en_frutas2)

if(__name__=="__main__"):
    main()
