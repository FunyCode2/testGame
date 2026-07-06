from classes.personaje import Personaje

class Arquero(Personaje):
  def __init__(self, nombre="Legolas", arco=3):
    super().__init__(nombre)
    self.arco = arco
    self.frz = self.frz * self.arco
    
  def atributos(self):
    self.stats()
    print(f"- Arco = {self.arco}")