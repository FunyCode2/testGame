from classes.caballero import Caballero
from classes.arquero import Arquero
from classes.mago import Mago
from classes.ladron import Ladron
from classes.berserker import Berserker
from classes.clerigo import Clerigo
from classes.necromante import Necromante
from classes.druida import Druida 

def crearPersonaje():
    
    print("\n" + "═" * 40)
    print("          CREACIÓN DE PERSONAJE  ")
    print("═" * 40)
    
    #Pedir nombre heroe
    nombre = input("Ingresa el nombre de tu héroe/heroina: ").strip()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Elige un nombre: ").strip()
    
    print("\nElige tu clase:")
    print("1. Caballero   🛡️ ")
    print("2. Arquero     🏹 ")
    print("3. Mago        🔮 ")
    print("4. Ladrón      🗡️ ")
    print("5. Berserker   🪓 ")
    print("6. Clérigo     ✨ ")
    print("7. Necromante  💀 ")
    print("8. Druida      🍃 ")

    opcion = ""
    while opcion not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        opcion = input("\nIntroduce el número de tu clase (1-8): ").strip()
        if opcion not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("❌ Opción inválida. Por favor, elige un número del 1 al 8.")

    print("\n✨ ¡Destino sellado! Tu personaje ha sido creado. ✨\n")

    if opcion == "1":
        return Caballero(nombre)
    elif opcion == "2":
        return Arquero(nombre)
    elif opcion == "3":
        return Mago(nombre)
    elif opcion == "4":
        return Ladron(nombre)
    elif opcion == "5":
        return Berserker(nombre)
    elif opcion == "6":
        return Clerigo(nombre)
    elif opcion == "7":
        return Necromante(nombre)
    elif opcion == "8":
        return Druida(nombre)