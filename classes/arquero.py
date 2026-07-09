from classes.personaje import Personaje

class Arquero(Personaje):
    """
    ARQUERO: Combatiente a distancia con arco y flechas. Ropa ligera de cuero.
    Ataca desde lejos y esquiva gracias a su agilidad.
    """

    def __init__(self, nombre="Marginado", arco=7):
        super().__init__(nombre)
        self.arco = arco

        # Fuerza + arco → daño de las flechas, moderado (suma, no multiplica)
        self.frz = self.frz + self.arco
        # Defensa + arco → su agilidad le permite esquivar ataques
        self.dfs = self.dfs + self.arco

    def atributos(self):
        self.stats()
        print(f"- arco = {self.arco}")