from classes.personaje import Personaje

class Ladron(Personaje):
    """
    LADRÓN: Asesino sigiloso con dos dagas. Capucha oscura, se mueve en las sombras.
    Poco daño por golpe, pero casi imposible de alcanzar.
    """

    def __init__(self, nombre="Marginado", dagas=5):
        super().__init__(nombre)
        self.dagas = dagas

        # Fuerza + dagas → dagas pequeñas, daño bajo por ataque
        self.frz = self.frz + self.dagas
        # Defensa × dagas → se esconde y esquiva, evasión muy alta
        self.dfs = self.dfs * self.dagas

    def atributos(self):
        self.stats()
        print(f"- dagas = {self.dagas}")