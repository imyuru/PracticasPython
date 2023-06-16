nombre = []
sexo = []
edad = []
tuple1=()
lista=[]
x=1
cantidadHombre=0
cantidadMujer=0
op1=0
cantidadMay21=0
while x!=0:
    while op1 != 2:
        nombre.append(str(input("Ingrese el nombre del estudiante: ")))
        sexo.append(str(input("Ingrese el sexo del estudiante (m/f): ")))
        edad.append(int(input("Ingrese la edad del estudiante: ")))
        op1 = int(input("Desea seguir ingresando estudiantes? 1. si  2. no :"))

    tuple1=(nombre,sexo,edad)


    print("1.Contar la cantidad de mujeres y hombres")
    print("2.Listar nombre de mujeres")
    print("3.Listar a personas con una edad x")
    print("4.Cantidad de estudiantes mayores a 21")
    op=int(input("Elija una opcion: "))

    match op:
        case 1:
            cantidadHombre=tuple1[1].count('m')
            cantidadMujer = tuple1[1].count('f')
            print(f"cantidad Mujer: {cantidadMujer}")
            print(f"cantidad Hombre: {cantidadHombre}")

        case 2:
            if 'f' in tuple1[1]:
                for i in tuple1[1]:
                    if i=='f':
                        print(tuple1[0][tuple1[1].index(i)])
        case 3:
            edadBuscada=int(input("Ingrese la edad que busca: "))
            for i in tuple1[2]:
                if i == edadBuscada:

                    print(tuple1[0][tuple1[2].index(i)])


        case 4:
            for i in tuple1[2]:
                if i > 21:
                    cantidadMay21+=1


            print(f"Cantidad de estudiantes mayores a 21: {cantidadMay21}")
            cantidadMay21=0