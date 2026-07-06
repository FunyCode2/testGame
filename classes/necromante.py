from classes.personaje import Personaje

class Necromante(Personaje):
  def __init__(self, nombre="Malakar", veneno=2):
    super().__init__(nombre)
    self.veneno = veneno
    self.magia = self.magia * self.veneno
    
  def atributos(self):
    self.stats()
    print(f"- Hecizo = venenos +{self.veneno}")