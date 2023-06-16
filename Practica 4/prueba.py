mi_tupla = ([1, 5, 3], [4, 5, 6], [7, 8, 9])
valor_a_contar = 5
cantidad_de_veces = 0

for lista in mi_tupla:
    cantidad_de_veces += lista.count(valor_a_contar)

print(cantidad_de_veces) # Salida: 1