class Silla:
    def __init__(self, tipo, precio):
        self._tipo = tipo
        self._precio = precio

    def calcular_descuento(self, cantidad):
        if self._tipo == "A":
            if cantidad >= 5:
                return self._precio * cantidad * 0.03
        elif self._tipo == "B":
            if cantidad >= 5:
                return self._precio * cantidad * 0.05
        elif self._tipo == "C":
            if cantidad >= 5:
                return self._precio * cantidad * 0.07

        return 0

    def calcular_total(self, cantidad):
        descuento = self.calcular_descuento(cantidad)
        total = self._precio * cantidad - descuento
        return total

    # Getters
    def get_tipo(self):
        return self._tipo

    def get_precio(self):
        return self._precio

    # Setters
    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_precio(self, precio):
        self._precio = precio


def main():
    tipo_sillas = {
        "A": 20,
        "B": 30,
        "C": 50
    }

    tipo = input("Ingrese el tipo de silla (A, B o C): ")
    cantidad = int(input("Ingrese la cantidad de sillas a comprar: "))

    if tipo not in tipo_sillas:
        print("Tipo de silla inválido")
        return

    precio = tipo_sillas[tipo]
    silla = Silla(tipo, precio)

    total = silla.calcular_total(cantidad)
    descuento = silla.calcular_descuento(cantidad)

    print("Tipo de silla: ", silla.get_tipo())
    print("Cantidad: ", cantidad)
    print("Precio: $", silla.get_precio())
    print("Descuento: $", descuento)
    print("Total a pagar: $", total)


if __name__ == "__main__":
    main()
