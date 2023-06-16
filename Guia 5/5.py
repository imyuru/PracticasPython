frutas=['melón', 'sandia', 'mango', 'piña','maracuya', 'guayaba']
print(frutas[1:4]) # Se extraen los elementos del 1 al 3. El 4 no es incluido.
print(frutas[3:]) # Se extraen todos los elementos de la lista a partir del que esta en la posición 3.
print(frutas[:4]) # Se extraen los elementos del 0 al 3.
print(frutas[:]) #Se extraen todos los elementos de la lista.
print(frutas[2::2]) # Se extraen los elementos a partir del elemento 2 hasta el final de la lista, pero se extraen de 2 en 2.
print(frutas[0:len(frutas)-1:3]) #Se extraen los elementos de la lista empezando en el elemento 0 hasta el final, extrayendo cada 3 elementos.
print(frutas[6:0:-2]) #Se extraen los elementos de la lista empezando en el último elemento hasta el elemento 0. extrayendo cada 2 elementos.