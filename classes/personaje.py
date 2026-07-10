import time

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
  
  def __init__(self, nombre="Marginado", frz=10, dfs=10, vida=100, nivel=1):
    self.nombre = nombre
    self.frz = frz
    self.dfs = dfs
    self.vida = vida
    self.nivel = nivel
  
  def stats(self): # Estadisticas del personaje
    print(f"- Nombre = {self.nombre}")
    print(f"- Fuerza = {self.frz}")
    print(f"- Defensa = {self.dfs}")
    print(f"- Vida = {self.vida}")
    print(f"- Nivel = {self.nivel}")
    print("=" * 50)
    
  def esta_vivo(self): # Verificar si el personaje esta vivo
    return self.vida > 0
  
  def __str__(self): # Nombre personaje
    return f"Nombre del personaje: {self.nombre}"
  
  
  
# Verificar si el personaje esta muerto ---------------------------------------------------------------------
  def morir(self): 
    self.vida = 0
    print("\n" + "☠️ " * 30)
    print("""
 ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
 ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
    """)
    print("☠️ " * 30)
    time.sleep(1)
    
    print(f"\nEl viaje de {self.nombre} ha llegado a su fin.")
    print("Tu cuerpo yace inerte en el frío suelo de Avalon, mientras las sombras")
    print("reclaman tu alma y cubren el reino en una noche eterna...")
    print("=" * 50)
  
  
  # Subir nivel de personaje ---------------------------------------------------------------------
  def subir_nivel(self, frz=0, dfs=0, vida=0, nivel=1):
    self.nivel += 1
    print("""
╔════════════════════════════════════╗
║          ¡LEVEL UP!                ║
╠════════════════════════════════════╣
║ ⭐ Has subido de nivel.            ║
║ 🎯 Nivel actual: {}                 ║
║ ⚔️ Ataque +5                        ║
║ 🛡️ Defensa +3                       ║
║ ❤️ Vida máxima +20                  ║
╚════════════════════════════════════╝
  """.format(self.nivel))
    self.frz = self.frz + 5
    self.dfs = self.dfs + 3
    self.vida = self.vida + 20



  def atacar(self, enemigo):
    dano = self.frz - enemigo.dfs
    
    if dano < 0: 
        dano = 0 
        
    enemigo.vida = enemigo.vida - dano
    print(("-" * 5) + "Inicia combate" + ("-" * 5))
    print(f"{self.nombre} ⚔️--> {enemigo.nombre}")
    print(f"💥 {enemigo.nombre} ha recibido {dano} de daño.")
    print("-" * 50)