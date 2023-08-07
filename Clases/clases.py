class Circulo:
    def __init__(self, radio):
        self.set_radio(radio)

    def set_radio(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radio = radio
        self.pi = 3.14159
        self.area = self.pi * radio ** 2
        self.perimetro = 2 * self.pi * radio

    def __str__(self):
        return f"Círculo con radio: {self.radio}, Área: {self.area}, Perímetro: {self.perimetro}"

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("El valor de multiplicación debe ser mayor que 0")
        return Circulo(self.radio * n)


nuevo_circulo = Circulo(6)

print("Círculo original:")
print(nuevo_circulo)

doble_circulo = nuevo_circulo * 2
print("\nCírculo duplicado:")
print(doble_circulo)

triple_circulo = nuevo_circulo * 3
print("\nCírculo triplicado:")
print(triple_circulo)

print("\nCambiando el radio del círculo original...")
nuevo_circulo.set_radio(8)
print(nuevo_circulo)
