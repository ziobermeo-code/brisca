import random
from constants import VALORES_CARTAS, PALOS, NUMEROS


NOMBRES_CARTAS = {
    1: 'As',
    10: 'Sota',
    11: 'Caballo',
    12: 'Rey',
}


class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def valor(self):
        """Retorna el valor de puntuacion de la carta."""
        return VALORES_CARTAS.get(self.numero, 0)

    def __repr__(self):
        """Representacion legible: 'As de oros', 'Rey de espadas', etc."""
        nombre = NOMBRES_CARTAS.get(self.numero, str(self.numero))
        return f'{nombre} de {self.palo}'


def crear_mazo():
    """Genera lista de 40 Cartas (4 palos x 10 numeros)."""
    return [Carta(numero, palo) for palo in PALOS for numero in NUMEROS]


def barajar_mazo(mazo):
    """Baraja el mazo usando random.shuffle."""
    random.shuffle(mazo)
