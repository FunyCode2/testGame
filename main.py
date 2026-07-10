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
from functions.crear_personajes import crearPersonaje



#-------------------------------------------------INICIO DE JUEGO---------------------------------------------------------------------------------------*
mostrar_bienvenida()

#------------------------------------------PERSONAJE DEL JUGADOR----------------------------------------------------*

heroe = crearPersonaje()
heroe.stats()

#heroe.subir_nivel()
#heroe.stats()

enemigo = Berserker("Sauron")
enemigo.stats()
#heroe.atacar(enemigo)
#enemigo.stats()

time.sleep(2)
print("\n¡Prepárate para la batalla! El enemigo se acerca...\n")
time.sleep(2)
print(f"⚔️  {heroe.nombre} VS {enemigo.nombre} ⚔️\n")
time.sleep(4)
print("¡Que comience el combate!\n")
time.sleep(2)
print("------------------------------------------------------------\n")


# ---  Combate  ---
while heroe.esta_vivo() and enemigo.esta_vivo():
    heroe.atacar(enemigo)

    if not enemigo.esta_vivo():
        print(f"\n💀 {enemigo.nombre} ha sido derrotado de forma definitiva.")
        heroe.subir_nivel()
        break               
        
    enemigo.atacar(heroe)
    
    if not heroe.esta_vivo():
        heroe.morir()
        break 