from classes.personaje import Personaje

class Necromante(Personaje):
    """
    NECROMANTE: Mago oscuro con cayado de huesos. Túnica morada, rostro oculto.
    Domina la magia prohibida y los muertos vivientes. Hechizos devastadores
    pero su cuerpo está debilitado por años de magia oscura.
    """

    def __init__(self, nombre="Marginado", cayado=9):
        super().__init__(nombre)
        self.cayado = cayado

        # Fuerza × cayado → hechizos oscuros muy potentes (daño alto)
        self.frz = self.frz * self.cayado
        # Vida - 3 → cuerpo frágil, la magia oscura le consume la salud
        self.vida = max(1, self.vida - 3)

    def atributos(self):
        self.stats()
        print(f"- cayado = {self.cayado}")