from classes.personaje import Personaje

class Berserker(Personaje):
    """
    BERSERKER: Guerrero salvaje sin armadura, solo piel de animal y un hacha gigante.
    Entra en furia y causa el mayor daño físico, pero casi no se defiende.
    """

    def __init__(self, nombre="Marginado", hacha=12):
        super().__init__(nombre)
        self.hacha = hacha

        # Fuerza × hacha → el mayor daño físico del juego
        self.frz = self.frz * self.hacha
        # Vida + hacha → resiste golpes con pura vitalidad, no con armadura
        self.vida = self.vida + self.hacha
        # Defensa - 3 → sin armadura, apenas bloquea ataques
        self.dfs = max(1, self.dfs - 3)

    def atributos(self):
        self.stats()
        print(f"- hacha = {self.hacha}")