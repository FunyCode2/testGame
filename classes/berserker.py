from classes.personaje import Personaje

class Berserker(Personaje):
  def __init__(self, nombre="Ragnar", hachas=4):
    super().__init__(nombre)
    self.hachas = hachas
    self.frz = self.frz * self.hachas
    
  def atributos(self):
    self.stats()
    print(f"- Hachas = {self.hachas}")