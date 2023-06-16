promedio,total,contar=0.0,0,0
mensaje="introduzca la nota del estudiante(-1 para salir):"
respuesta= int(input(mensaje))
while respuesta!=-1:
    total=total+respuesta
    contar=contar+1
    respuesta=int(input(mensaje))
else:
    promedio=total/contar
    print("promedio de notas: "+ str(promedio))
