import time
import sys

from classes.caballero import Caballero
from functions.bienvenida import mostrar_bienvenida
from functions.crear_personajes import crearPersonaje
from functions.menu_inicio import menu_inicio
from functions.clases import clases



#-------------------------------------------------MENU DE INICIO ---------------------------------------------------------------------------------------*

opcion = menu_inicio()

if opcion == "1":
    print("\n¡Has elegido iniciar una nueva aventura!")
    time.sleep(1)
    mostrar_bienvenida()
elif opcion == "2":
    print("\n¡Has elegido ver las clases disponibles!")
    time.sleep(1)
    clases()
elif opcion == "0":
    print("\n¡Gracias por jugar! Hasta la próxima aventura.")
else:
    print("\n❌ Opción inválida. Por favor, elige una opción válida del menú.")
    sys.exit(1)
    

#------------------------------------------PERSONAJE DEL JUGADOR----------------------------------------------------*

heroe = crearPersonaje()
heroe.stats()

#heroe.subir_nivel()
#heroe.stats()

enemigo = Caballero("Sauron")
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
