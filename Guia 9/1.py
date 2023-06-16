#Se define una Funcion para Sumar
def sumaNumeros (numero1, numero2):
    return numero1+ numero2
#Se llama la función
a =int(input("Introducir el primer numero entero"))
b=int(input("Introducir el segundo numero entero"))
resultado= sumaNumeros(a, b)
print(resultado)