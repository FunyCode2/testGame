from classes.personaje import Personaje

class Clerigo(Personaje):
  def __init__(self, nombre="Lumiel", sanacion=5):
    super().__init__(nombre)
    self.sanacion = sanacion
    self.vida = self.vida + self.sanacion
    
  def atributos(self):
    self.stats()
    print(f"- Sanacion = +{self.sanacion}")