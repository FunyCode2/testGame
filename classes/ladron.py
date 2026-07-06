from classes.personaje import Personaje

class Ladron(Personaje):
  def __init__(self, nombre="Gollum", navajas=3):
    super().__init__(nombre)
    self.navajas = navajas
    self.frz = self.frz * self.navajas
    
  def atributos(self):
    self.stats()
    print(f"- Navajas = {self.navajas}")