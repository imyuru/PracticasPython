def escribirnombre (*nombres):
    for nom in nombres:
        print(nom)
nom1= input("Introducir un nombre: ")
nom2= input("Introducir un nombre: ")
nom3= input ("Introducir un nombre: ")
escribirnombre(nom1, nom2, nom3)
print("Enviando un solo valor")
escribirnombre(nom3)