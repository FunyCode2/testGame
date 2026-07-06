from classes.personaje import Personaje

class Mago(Personaje):
  def __init__(self, nombre="Gandalf", magia=8):
    super().__init__(nombre)
    self.magia = magia
    self.magia = self.magia * self.magia
    
  def atributos(self):
    self.stats()
    print(f"- Hechizo = {self.magia}")