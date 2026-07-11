def combate (heroe, enemigo):
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