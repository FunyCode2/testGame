from classes.personaje import Personaje
from classes.caballero import Caballero
from classes.arquero import Arquero
from classes.mago import Mago

heroe = Caballero()

heroe.stats()

heroe.subir_nivel(5, 2, 2)
heroe.stats()

enemigo = Personaje("Sauron", vida=50)
enemigo.stats()
heroe.atacar(enemigo)
enemigo.stats()