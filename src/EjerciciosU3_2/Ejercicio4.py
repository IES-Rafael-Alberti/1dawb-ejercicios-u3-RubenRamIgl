def mesDiccionario(numeroMes):
    meses={
        1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo",
        6: "junio", 7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre",
        11: "noviembre", 12: "diciembre"
    }

    return meses.get(numeroMes, "mes no válido")

def pedirFecha():
    fecha=input("Introduce una fecha(dd/mm/aaa): ")

    try:
        partesFecha=fecha.split("/")
        dia=int(partesFecha[0])
        mes=int(partesFecha[1])
        año=int(partesFecha[2])

        nombreMes=mesDiccionario(mes)

        print(f"{dia} de {nombreMes} de {año}")
    except ValueError:
        print("Formato de fecha no válido. Utiliza dd/mm/aaaa")

def main():
    pedirFecha()

if(__name__=="__main__"):
    main()