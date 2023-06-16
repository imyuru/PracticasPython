def saludoso (nombre, titulo='Sr(a)'):
    print(f"{titulo}{nombre}")
nom=input("Introducir el nombre:")
tit=input('Introducir el tratamiento (Sr. Sra.):')
saludoso(nom, tit)