import time

def menu_inicio():
  print("\n" + "═" * 60)
  print("                 ⚔️  CRÓNICAS DE AVALON  ⚔️")
  print("═" * 60)
  time.sleep(0.5)

  print("\nHas cruzado el umbral del reino.")
  print("Las antiguas tierras aguardan tu decisión...")
  time.sleep(1)

  print("\n" + "─" * 60)
  print("                 MENÚ PRINCIPAL")
  print("─" * 60)
  print("  [1] 🗡 Nueva aventura")
  print("  [2] 📖 Ver clases")
  print("  [0] 🚪 Salir")
  print("─" * 60)

  opcion = input("\n¿Qué deseas hacer? ➜ ")

  return opcion