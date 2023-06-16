ingreso= float(input("ingrese el monto de su ingreso anual:"))
hijos= int(input("Ingrese la cantidad de hijos que tiene:"))
if(ingreso>=12000)or(10000 <ingreso<12000 and hijos<=2)or (8000<=ingreso<=10000 and hijos==0):
    print("credito aprobado")
else:
    print("credito no aprobado")