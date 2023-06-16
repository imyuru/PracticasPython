animales = []
i = 0
pos = 0
izquiera = 0
derecha = 0
while i < 10:
    animales.append(input("Ingrese un animal: ").lower())
    i += 1
animalBuscado = str(input("Ingrese el animal a buscar: "))
for x in range(len(animales)):
    if animalBuscado == animales[x]:
        pos = x
        izquiera = x - 1
        derecha = x + 1

print("Animal buscado: " + animales[pos])
print("Animal a la izquierda: " + animales[izquiera])
print("Animal a la derecha: " + animales[derecha])
