"""
Clase base para los personajes del juego.

Atributos:
- nombre
- fuerza
- defensa
- vida
"""

class Personaje:
  #atributos
    #nombre = "Marginado"
    #frz = 10 fuerza
    #dfs = 10 defensa
    #vida = 10
  
  def __init__(self, nombre="Marginado", frz=10, dfs=10, vida=10):
    self.nombre = nombre
    self.frz = frz
    self.dfs = dfs
    self.vida = vida