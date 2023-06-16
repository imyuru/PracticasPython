while True:
  x=input("Ingrese un numero ('-' para terminar): ")
  print(x)
  if x=='-':
    break
  elif x>'0':
    print("Numero positivo")
  elif x=='0':
    print("Igual a 0")
  elif x<'0':
    print("Numero negativo")