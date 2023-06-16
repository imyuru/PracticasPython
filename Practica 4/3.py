calificaciones=[]
sexo=[]
nombres=[]
x=1
op1 = 0
notaMinimaHombre = float('inf')
nombreMinimoHombre = ""
notaMinimaMujer = float('inf')
nombreMinimaMujer = ""

notaMaxHombre = float('inf')
nombreMaxHombre = ""
notaMaxMujer = float('inf')
nombreMaxMujer = ""

cantidad=0.0
while x!=0 :
    while op1 != 2:
        nombres.append(str(input("Ingrese el nombre del estudiante: ")))
        calificaciones.append(float(input("La calificacion: ")))
        sexo.append(str((input("Ingrese el sexo del estudiante  masculino/femenino: ")).lower()))
        op1=int(input("Desea seguir ingresando estudiantes? 1. si  2. no :"))

    print("Bienvenido al sistema")
    print("1.Devuelva la nota mas alta obtenida y a quien pertenece")
    print("2.Nota mínima obtenida por los hombres y la nota mínima obtenida por las mujeres")
    print("3.Nota promedio")
    print("4.Devuelva cuantas calificaciones están por debajo del promedio")
    print("5.Quienes obtuvieron mejores calificaciones hombres o mujeres")
    print("6.Salir")
    op = int(input("Ingrese una opcion: "))

    match op:
        case 1:
            posicion= calificaciones.index(max(calificaciones))

            print(f"Estudiantes con mayor calificacion {nombres[posicion]} con {calificaciones[posicion]}")

        case 2:
            for i in range(len(calificaciones)):
                if 'masculino' in sexo:
                    if sexo[i] == 'masculino' and calificaciones[i] < notaMinimaHombre:
                        notaMinimaHombre = calificaciones[i]
                        nombreMinimoHombre = nombres[i]
                if 'femenino' in sexo:
                  if sexo[i] == 'femenino' and calificaciones[i] < notaMinimaMujer:
                        notaMinimaMujer = calificaciones[i]
                        nombreMinimaMujer = nombres[i]

            if 'masculino' in sexo:
                print(f"Nota minima Hombres {notaMinimaHombre} le pertenece a {nombreMinimoHombre}")
            else:
                print("NO EXISTEN HOMBRES EN LA LISTA")
            if 'femenino' in sexo:
                print(f"Nota minima Hombres {notaMinimaMujer} le pertenece a {nombreMinimaMujer}")
            else:
                print("NO EXISTEN MUJERES EN LA LISTA")
        case 3:
            for i in calificaciones:
                cantidad+=i
            promedio=cantidad/len(calificaciones)
            print(f"El promedio de calificaciones es {promedio}")


        case 4:
            for i in calificaciones:
                cantidad += i
            promedio = cantidad / len(calificaciones)
            print(f"El promedio de calificaciones es {promedio}")
            print("Calificaciones menores al promedio")
            for nomb,nota,sexos in zip(nombres,calificaciones,sexo):
                if nota<promedio:
                    print(nomb,nota,sexos)


            cantidad = 0.0
        case 5:
            for i in range(len(calificaciones)):
                if 'masculino' in sexo:
                    if sexo[i] == 'masculino' and calificaciones[i] > notaMaxHombre:
                        notaMaxHombre = calificaciones[i]
                        nombreMaxHombre = nombres[i]
                if 'femenino' in sexo:
                    if sexo[i] == 'femenino' and calificaciones[i] > notaMaxMujer:
                        notaMaxMujer = calificaciones[i]
                        nombreMaxMujer = nombres[i]

            if 'masculino' in sexo:
                print(f"Nota maxima Hombres {notaMaxHombre} le pertenece a {nombreMaxHombre}")
            else:
                print("NO EXISTEN HOMBRES EN LA LISTA")
            if 'femenino' in sexo:
                print(f"Nota minima Hombres {notaMaxMujer} le pertenece a {nombreMaxMujer}")
            else:
                print("NO EXISTEN MUJERES EN LA LISTA")

        case 6:
            print("Saliendo")
            x=0

        case _:
            print("elija una opcion correcta")