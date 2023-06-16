nombre = []
sexo = []
estatura = []
peso = []
hombres = []
mujeres = []
totalPesosM = 0.0
totalPesosF = 0.0
NEMayorM = ""
NEMayorF = ""
eMayorM = 0.0
eMayorF = 0.0
estaturas_m = []
estaturas_f = []
nombres_m = []
nombres_f = []
peso_m = []
peso_f = []
bajoPesoPromedioM = []
bajoPesoPromedioF = []
promedioM = 0.0
promedioF = 0.0
estaturaM = 0.0
estaturaF = 0.0
promedioEM = 0.0
promedioEF = 0.0

cantidad = int(input("Ingrese la cantidad de estudiantes"))

x = 0
while x < cantidad:
    nombre.append(input("Ingrese el nombre del estudiante "))
    sexo.append(input("Ingrese el sexo del estudiante m/f ").lower())
    estatura.append(input("Ingrese la estatura del estudiante "))
    peso.append(input("Ingrese el peso del estudiante "))
    if sexo[x] == "m":
        totalPesosM += float(peso[x])
        estaturaM += float(estatura[x])
    elif sexo[x] == "f":
        totalPesosF += float(peso[x])
        estaturaF += float(estatura[x])
    x += 1

for i in range(len(estatura)):
    if sexo[i] == 'm':
        estaturas_m.append(estatura[i])
        nombres_m.append(nombre[i])
        peso_m.append(peso[i])
    elif sexo[i] == 'f':
        estaturas_f.append(estatura[i])
        nombres_f.append(nombre[i])
        peso_f.append(peso[i])

cantidadM = sexo.count("m")
cantidadF = sexo.count("f")

print(f"Cantidad de estudiantes M :{cantidadM}")
print(f"Cantidad de estudiantes F :{cantidadF}")

if cantidadM > 0:
    promedioM = float(totalPesosM / cantidadM)
    promedioEM = float(estaturaM / cantidadM)
if cantidadF > 0:
    promedioF = float(totalPesosF / cantidadF)
    promedioEF = float(estaturaF / cantidadM)

for i in range(len(peso_m)):
    if float(peso_m[i]) < promedioM:
        bajoPesoPromedioM.append(nombres_m[i])

for i in range(len(peso_f)):
    if float(peso_f[i]) < promedioF:
        bajoPesoPromedioF.append(nombres_f[i])

print(f"Promedio peso M :{promedioM}")
print(f"Promedio peso F :{promedioF}")
print(f"Promedio estatura M :{promedioEM}")
print(f"Promedio peso F :{promedioEF}")

if estaturas_m:
    maxMNombre = nombres_m[estaturas_m.index(max(estaturas_m))]
    print(f"Estudiante con mayor estatura Hombre : {maxMNombre}")
    print(f"Estudiantes bajo del promedio de Masculino : {bajoPesoPromedioM}")
if estaturas_f:
    maxFNombre = nombres_f[estaturas_f.index(max(estaturas_f))]
    print(f"Estudiante con mayor estatura Mujer : {maxFNombre}")
    print(f"Estudiantes bajo del promedio de peso Femenina : {bajoPesoPromedioF}")
