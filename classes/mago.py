from classes.personaje import Personaje

class Mago(Personaje):
    """
    MAGO: Hechicero con túnica y bastón mágico. Lanza hechizos de fuego/hielo.
    Potente a distancia pero muy frágil si un enemigo lo alcanza.
    """

    def __init__(self, nombre="Marginado", baston=8):
        super().__init__(nombre)
        self.baston = baston

        # Fuerza + bastón → el poder de sus hechizos se representa como fuerza
        self.frz = self.frz + self.baston
        # Vida + bastón → su maná (energía mágica) se representa como vida extra
        self.vida = self.vida + self.baston
        # Defensa - 2 → sin armadura, apenas se defiende de ataques físicos
        self.dfs = max(1, self.dfs - 2)

    def atributos(self):
        self.stats()
        print(f"- baston = {self.baston}")