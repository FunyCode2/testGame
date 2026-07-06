from classes.personaje import Personaje

class Druida(Personaje):
  def __init__(self, nombre="Sylvan", resistencia=4):
    super().__init__(nombre)
    self.resistencia = resistencia
    self.dfs = self.dfs + self.resistencia
    
  def atributos(self):
    self.stats()
    print(f"- Resistencia = +{self.resistencia}")