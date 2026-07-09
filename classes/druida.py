from classes.personaje import Personaje

class Druida(Personaje):
    """
    DRUIDA: Guardián de la naturaleza con vara de madera viva. Cuernos de ciervo,
    barba blanca. Usa magia de la tierra y los animales. Equilibrado en todo,
    sin ser el mejor en nada pero sin debilidades graves.
    """

    def __init__(self, nombre="Marginado", vara=7):
        super().__init__(nombre)
        self.vara = vara

        # Fuerza + vara → magia de naturaleza con daño moderado
        self.frz = self.frz + self.vara
        # Vida + vara → la conexión con la tierra le da resistencia
        self.vida = self.vida + self.vara
        # Defensa + mitad de vara → la naturaleza le da algo de protección
        self.dfs = self.dfs + (self.vara // 2)

    def atributos(self):
        self.stats()
        print(f"- vara = {self.vara}")