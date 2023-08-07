class Circulo:
    """
    Clase que representa un círculo.
    """

    def __init__(self, radio):
        """
        Inicializa un círculo con el radio especificado utilizando el método .set_radio()

        Args:
            radio (float): El radio del círculo.
        """
        self.set_radio(radio)

    def set_radio(self, radio):
        """
        Define la funcion para establecer el radio del Círculo, se usa en primera instancia y tambien para editarlo una vez el Círculo ya exista.

        Args:
            radio (float): El nuevo radio del círculo.

        Raises:
            ValueError: Si el radio es menor o igual a 0.

        Ejemplos:
            >>> c = Circulo(2.5)
            >>> c.radio
            2.5
            >>> c.area
            19.6349375
            >>> c.perimetro
            15.70795
        """
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.radio = radio
        self.pi = 3.14159
        self.area = self.pi * radio ** 2
        self.perimetro = 2 * self.pi * radio

    def __str__(self):
        """
        Devuelve una representación en cadena del círculo.

        Returns:
            str: Representación del círculo.
        """
        return f"Círculo con radio: {self.radio}, Área: {self.area}, Perímetro: {self.perimetro}"

    def __mul__(self, n):
        """
        Multiplica el radio del círculo por un factor.

        Args:
            n (float): Factor de multiplicación.

        Returns:
            Circulo: Nuevo círculo con el radio multiplicado.

        Raises:
            ValueError: Si el valor de multiplicación es menor o igual a 0.

        Ejemplos:
            >>> c = Circulo(2)
            >>> nuevo_circulo = c * 3
            >>> nuevo_circulo.radio
            6
        """
        if n <= 0:
            raise ValueError("El valor de multiplicación debe ser mayor que 0")
        return Circulo(self.radio * n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


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
