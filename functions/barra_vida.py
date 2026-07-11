def barra_vida(valor):
    """
    Genera una barra de progreso de 20 bloques.
    Cada bloque representa 5 puntos.
    """
    llenos = valor // 5
    vacios = 20 - llenos
    return "█" * llenos + "░" * vacios