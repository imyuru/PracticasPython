class Comerciante:
    def __init__(self, calidad,cantidad):

        self._calidad = calidad
        self._cantidad= cantidad

    def get_calidad(self):
        return self._calidad


    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad


    def set_calidad(self, calidad):
        self._calidad = calidad


    def descuento(self):
        descuento=0.0
        if comerciante.get_calidad()==str("a"):
            descuento=float(comerciante.get_cantidad())*0.03
        if comerciante.get_calidad() == str("b"):
            descuento = float(comerciante.get_cantidad()) * 0.05
        if comerciante.get_calidad() == str("c"):
            descuento = float(comerciante.get_cantidad()) * 0.07
        return descuento

    def main(self):
        preciototal=0.0
        precio=0.0
        print("A.$20 B.$30 C.$50")
        comerciante.set_calidad((str(input("Ingrese el tipo de silla"))).lower())
        comerciante.set_cantidad((input("Ingrese la cantidad")))
        descuento=comerciante.descuento()
        print(comerciante.get_calidad())
        match str(comerciante.get_calidad()):
            case "a":
                precio = 20.0
                preciototal=precio-descuento
            case "b":
                precio=30.0
                preciototal = precio - descuento
            case "c":
                precio = 50.0
                preciototal = precio - descuento

        print(f"Tipo de silla comprada {comerciante.get_calidad()}")
        print(f"Cantidad comprada {comerciante.get_cantidad()}")
        print(f"Precio Por Unidad {precio}")
        print(f"Descuento {descuento}")
        print(f"Precio Total {preciototal*float(comerciante.get_cantidad())}")



if __name__ == '__main__':
    comerciante = Comerciante("a",0)
    comerciante.main()



