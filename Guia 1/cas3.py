año=int(input(("introduzca el año: ")))
mes=input("introduzca el mes").lower()
match mes:
    case "enero"|"marzo"|"julio"|"agosto"|"octubre"|"diciembre":
        print("tiene 31 dias")
    case "abril"|"junio"|"septiembre"|"noviembre":
        print("tiene 30 dias")
    case "febrero":
        c=año%4
        if año%4==0:
            print("Tiene 29 dias")
        else:
            print("tiene 28 dias")
    case _:
        print("valor invalido")

