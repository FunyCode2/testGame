import time

from classes.personaje import Personaje
from classes.caballero import Caballero
from classes.arquero import Arquero
from classes.mago import Mago
from classes.ladron import Ladron
from classes.berserker import Berserker
from classes.clerigo import Clerigo
from classes.necromante import Necromante
from classes.druida import Druida
from functions.bienvenida import mostrar_bienvenida

mostrar_bienvenida()

heroe = Caballero("Sir Lancelot")
heroe.stats()

#heroe.subir_nivel(5, 2, 2)
#heroe.stats()

enemigo = Berserker("Sauron")
enemigo.stats()
#heroe.atacar(enemigo)
#enemigo.stats()

while heroe.esta_vivo() and enemigo.esta_vivo():
    heroe.atacar(enemigo)
    enemigo.atacar(heroe)