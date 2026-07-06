from classes.personaje import Personaje

class Caballero(Personaje):
  def __init__(self, nombre="Aragorn", espada=5):
    super().__init__(nombre)  # hereda nombre, frz, dfs y vida
    self.espada = espada
    # Caballero = daño: fuerza base × poder de la espada
    self.frz = self.frz * self.espada

  def atributos(self):
    self.stats()
    print(f"- espada = {self.espada}")
