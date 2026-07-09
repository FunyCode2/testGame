from classes.personaje import Personaje

class Caballero(Personaje):
    """
    CABALLERO: Guerrero con armadura de placas, espada y escudo.
    Es el tanque del grupo: pelea cuerpo a cuerpo y aguanta en la línea frontal.
    """

    def __init__(self, nombre="Marginado", espada=10):
        super().__init__(nombre)
        self.espada = espada

        # Fuerza × espada → la espada es un arma pesada, su daño se multiplica
        self.frz = self.frz * self.espada

    def atributos(self):
        self.stats()
        print(f"- espada = {self.espada}")
