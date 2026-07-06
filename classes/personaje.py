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
  
  def __init__(self, nombre="Marginado", frz=10, dfs=10, vida=10, magia=0):
    self.nombre = nombre
    self.frz = frz
    self.dfs = dfs
    self.vida = vida
    self.magia = magia
  
  def stats(self): # Estadisticas del personaje
    print(f"- Nombre = {self.nombre}")
    print(f"- Fuerza = {self.frz}")
    print(f"- Defensa = {self.dfs}")
    print(f"- Vida = {self.vida}")
    print("=" * 50)
    
  def subir_nivel(self, frz=0, dfs=0, vida=0): # Subir nivel de personaje
    print("🎉 ¡FELICIDADES!")
    print("⭐ Has subido de nivel")
    self.frz = self.frz + frz
    self.dfs = self.dfs + dfs
    self.vida = self.vida + vida
    
  def esta_vivo(self): # Verificar si el personaje esta vivo
    return self.vida > 0

  def morir(self): # Verificar si el personaje esta muerto
    self.vida = 0
    print(f"{self.nombre} ha estirado la pata.")

  def __str__(self): # Nombre personaje
    return f"Nombre del personaje: {self.nombre}"

  def atacar(self, enemigo):
    dano = self.frz - enemigo.dfs
    enemigo.vida = enemigo.vida - dano
    print(f"{self.nombre} --> {enemigo.nombre}")
    print(f"{enemigo.nombre} ha recibido {dano} de daño")
    if not enemigo.esta_vivo():
      enemigo.morir()
    print("-" * 50)