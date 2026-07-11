from classes.personaje import Personaje
from functions.barra_vida import barra_vida

class Caballero(Personaje):
    """
    CABALLERO: Guerrero con armadura de placas, espada y escudo.
    Es el tanque del grupo: pelea cuerpo a cuerpo y aguanta en la línea frontal.
    """

    def __init__(self, nombre="Marginado", espada=10):
        super().__init__(nombre)
        self.espada = espada

        # Fuerza × espada → la espada es un arma pesada, su daño se multiplica
        self.frz = self.frz * self.espada

    def atributos(self):
        self.stats()
        print(f"- espada = {self.espada}")
        
    def graficoAtributos(self):
        print(f"""
════════════════════════════════════════════════════
                ⚔️ GUERRERO
════════════════════════════════════════════════════

"El escudo del reino y la primera línea de batalla."

(f"Vida        {barra_vida(100)} 100")
(f"Ataque      {barra_vida(80)}  80")
(f"Defensa     {barra_vida(90)}  90")
(f"Magia       {barra_vida(20)}  20")
(f"Velocidad   {barra_vida(50)}  50")

Habilidad especial:
► Golpe Demoledor
Inflige un poderoso ataque con posibilidad de aturdir
al enemigo.

════════════════════════════════════════════════════

Presiona ENTER para volver...
        """)