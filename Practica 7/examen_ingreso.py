examingreso = {}
w = 0
examingreso.update({'identificacion': [], 'nombre': [], 'puntaje': []})
while True:
    print("1. Registrar Estudiantes")
    print("2. Consulta de Estudiantes con Mayor Puntaje")
    print("3. Consulta de Estudiantes con Menor Puntaje")
    print("4. Consultar Estudiante por Identificación")
    print("5. Consultar Puntaje Promedio Obtenido")
    print("6. Consulta de Estudiantes que aprobaron el examen")
    print("7. Salir")

    opcion = str(input("Ingrese una opción:"))
    match opcion:
        case '1':
            identificacion = input("Ingrese la identificación del estudiante: ")
            nombre = input("Ingrese el nombre del estudiante: ")
            puntaje = float(input("Ingrese el puntaje obtenido: "))
            examingreso.get("identificacion").append(identificacion)
            examingreso.get("nombre").append(nombre)
            examingreso.get("puntaje").append(puntaje)
            print("Estudiante Registrado")
        case '2':
            maximo = max(examingreso.get("puntaje"))
            nombreMaxPos = examingreso.get("puntaje").index(maximo)
            nombreMax = examingreso.get("nombre")[nombreMaxPos]
            print(f"El estudiante con mayor puntaje es {nombreMax} con {maximo}")
        case '3':
            min = min(examingreso.get("puntaje"))
            nombreMinPos = examingreso.get("puntaje").index(min)
            nombreMin = examingreso.get("nombre")[nombreMinPos]
            print(f"El estudiante con Menor puntaje es {nombreMin} con {min}")
        case '4':
            iDBuscar = input("Ingrese el id del estudiante a buscar")
            idPos = examingreso.get("identificacion").index(iDBuscar)
            nombreIDPos = examingreso.get("nombre")[idPos]
            puntajePos = examingreso.get("puntaje")[idPos]
            print(f"Identificacion:{iDBuscar} | Nombre: {nombreIDPos} | Puntaje:{puntajePos}")
        case '5':
            for x in range(len(examingreso.get("puntaje"))):
                w += examingreso.get("puntaje")[x]

            promedio = w / len(examingreso.get("puntaje"))

            print(f'Puntaje promedio {promedio}')
        case '6':
            for x in range(len(examingreso.get("puntaje"))):
                if examingreso.get("puntaje")[x] >= 80:
                    print(f'{examingreso.get("identificacion")[x]} :{examingreso.get("nombre")[x]} '
                          f'{examingreso.get("puntaje")[x]}')
        case '7':
            print("Gracias por venir")
            break
