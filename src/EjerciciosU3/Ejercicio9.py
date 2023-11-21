def pedirPalabra():
    palabra=input("Introduce una palabra: ")

    return palabra

def contarVocales(palabra):
    cuenta_a=0
    cuenta_e=0
    cuenta_i=0
    cuenta_o=0
    cuenta_u=0

    for letra in palabra:
        letra_min=letra.lower()

        if(letra_min=="a"):
            cuenta_a+=1
        elif(letra_min=="e"):
            cuenta_e+=1
        elif(letra_min=="i"):
            cuenta_i+=1
        elif(letra_min=="o"):
            cuenta_o+=1
        elif(letra_min=="u"):
            cuenta_u+=1

    return cuenta_a, cuenta_e, cuenta_i, cuenta_o, cuenta_u

def main():
    palabra=pedirPalabra()
    cuenta_a, cuenta_e, cuenta_i, cuenta_o, cuenta_u=contarVocales(palabra)

    print(f"La vocal a aparece {cuenta_a} veces.")
    print(f"La vocal e aparece {cuenta_e} veces.")
    print(f"La vocal i aparece {cuenta_i} veces.")
    print(f"La vocal o aparece {cuenta_o} veces.")
    print(f"La vocal u aparece {cuenta_u} veces.")

if(__name__=="__main__"):
    main()