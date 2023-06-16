def operacion(n1, n2):
    s= n1+n2
    r=n1-n2
    m=n1*n2
    return (s,r,m)
num1=int(input("Introducir un número entero:"))
num2=int(input("Introducir un número entero:"))
res=operacion(num1,num2)
print(f"El resultado es: {res}")
print(f"El resultado de la suma es: {res[0]}")
print(f"El resultado de la resta es: {res[1]}")
print(f"El resultado de la multiplicacion es: {res[2]}")