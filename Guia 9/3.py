def factoria(num):
    resultado= num
    for i in range(num - 1, 1, -1):
        resultado = resultado*i
    return resultado

num=int(input ("Introducir un numero entero:"))
print(factoria(num))