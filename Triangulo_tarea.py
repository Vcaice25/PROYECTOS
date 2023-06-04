class Figura:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    @property
    def area(self):
        return 0.5 * self.base * self.altura

    @property
    def perimetro(self):
        return 3 * self.base