dia=int(input("Introduzca un numero entre 1 y el 7"))
match dia:
    case 1:
        print("lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Doming")
    case _:
        print("el numero introducido no corresponde a ningun dia")