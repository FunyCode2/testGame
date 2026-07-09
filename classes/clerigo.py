from classes.personaje import Personaje

class Clerigo(Personaje):
    """
    CLÉRIGO: Sacerdote guerrero con maza y escudo sagrado. Túnica blanca con cruz dorada.
    Cura aliados y aguanta en el frente. No es el que más daño hace, pero es muy resistente.
    """

    def __init__(self, nombre="Marginado", maza=6):
        super().__init__(nombre)
        self.maza = maza # Que es maza? Es como un cetro o un baston.

        # Fuerza + mitad de maza → ataque moderado, su rol no es ser el mayor daño
        self.frz = self.frz + (self.maza // 2)
        # Defensa + maza → escudo sagrado y armadura ligera lo protegen
        self.dfs = self.dfs + self.maza
        # Vida + maza → puede curarse a sí mismo, aguanta más golpes
        self.vida = self.vida + self.maza

    def atributos(self):
        self.stats()
        print(f"- maza = {self.maza}")