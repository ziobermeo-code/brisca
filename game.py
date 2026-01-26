from deck import Carta, crear_mazo, barajar_mazo
from constants import FUERZA_CARTAS


class Brisca:
    """Motor del juego de la Brisca para 2-4 jugadores."""

    def __init__(self, jugadores):
        if not 2 <= len(jugadores) <= 4:
            raise ValueError("La Brisca requiere entre 2 y 4 jugadores")

        self.jugadores = jugadores
        self.mazo = []
        self.triunfo = None             # Carta que define el palo de triunfo
        self.palo_triunfo = None        # Palo de triunfo (se mantiene tras recoger carta)
        self.mesa = []                  # Lista de tuplas (jugador, carta)
        self.turno_actual = 0
        self.mano_inicial = 0           # Quién inició la baza

    def iniciar_partida(self):
        """Inicia una nueva partida: baraja, reparte y define triunfo."""
        # Resetear estado de jugadores
        for jugador in self.jugadores:
            jugador.mano = []
            jugador.puntos = 0
            jugador.bazas_ganadas = []

        # Crear y barajar mazo
        self.mazo = crear_mazo()
        barajar_mazo(self.mazo)

        # En partidas de 3 jugadores, quitar una carta (el 2 de oros)
        # para que 39 cartas se dividan exactamente entre 3
        if len(self.jugadores) == 3:
            self.mazo = [c for c in self.mazo if not (c.numero == 2 and c.palo == 'oros')]

        # Repartir 3 cartas a cada jugador
        self.repartir()

        # La siguiente carta define el triunfo
        self.triunfo = self.mazo.pop()
        self.palo_triunfo = self.triunfo.palo

        # Resetear estado de la mesa
        self.mesa = []
        self.turno_actual = 0
        self.mano_inicial = 0

    def repartir(self):
        """Reparte 3 cartas a cada jugador."""
        for _ in range(3):
            for jugador in self.jugadores:
                if self.mazo:
                    carta = self.mazo.pop()
                    jugador.recibir_carta(carta)

    def jugador_actual(self):
        """Devuelve el jugador que tiene el turno."""
        return self.jugadores[self.turno_actual]

    def jugar_carta(self, jugador, indice_carta):
        """
        Un jugador juega una carta de su mano.
        Retorna True si la carta se jugó correctamente.
        """
        if jugador != self.jugador_actual():
            return False

        carta = jugador.jugar_carta(indice_carta)
        if carta is None:
            return False

        self.mesa.append((jugador, carta))

        # Avanzar turno
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)

        return True

    def baza_completa(self):
        """Retorna True si todos los jugadores han jugado."""
        return len(self.mesa) == len(self.jugadores)

    def resolver_baza(self):
        """
        Resuelve la baza actual.
        Retorna el jugador ganador.
        """
        if not self.baza_completa():
            return None

        ganador = self._determinar_ganador_baza()

        # Sumar puntos al ganador
        puntos_baza = sum(carta.valor() for _, carta in self.mesa)
        ganador.puntos += puntos_baza

        # Guardar cartas ganadas
        for _, carta in self.mesa:
            ganador.bazas_ganadas.append(carta)

        # Limpiar mesa
        self.mesa = []

        # El ganador inicia la siguiente baza
        self.turno_actual = self.jugadores.index(ganador)
        self.mano_inicial = self.turno_actual

        return ganador

    def _determinar_ganador_baza(self):
        """Determina qué jugador gana la baza actual."""
        palo_salida = self.mesa[0][1].palo
        ganador, carta_ganadora = self.mesa[0]

        for jugador, carta in self.mesa[1:]:
            if self._carta_gana(carta, carta_ganadora, palo_salida):
                carta_ganadora = carta
                ganador = jugador

        return ganador

    def _carta_gana(self, carta, ganadora, palo_salida):
        """
        Determina si 'carta' gana a 'ganadora'.
        Reglas:
        1. Triunfo siempre gana a no-triunfo
        2. Entre triunfos o mismo palo, gana la de mayor fuerza
        3. Carta que no es triunfo ni palo de salida nunca gana
        """
        es_triunfo = carta.palo == self.palo_triunfo
        ganadora_es_triunfo = ganadora.palo == self.palo_triunfo

        # Triunfo vs no-triunfo
        if es_triunfo and not ganadora_es_triunfo:
            return True
        if ganadora_es_triunfo and not es_triunfo:
            return False

        # Ambas son triunfo
        if es_triunfo and ganadora_es_triunfo:
            return FUERZA_CARTAS[carta.numero] > FUERZA_CARTAS[ganadora.numero]

        # Ninguna es triunfo
        if carta.palo == palo_salida and ganadora.palo == palo_salida:
            return FUERZA_CARTAS[carta.numero] > FUERZA_CARTAS[ganadora.numero]

        # Carta no es del palo de salida, nunca gana
        return False

    def robar_cartas(self):
        """
        Los jugadores roban cartas del mazo.
        El ganador de la baza roba primero.
        """
        if not self.mazo and not self.triunfo:
            return

        # Orden de robo: empezando por quien ganó la baza
        orden = []
        for i in range(len(self.jugadores)):
            indice = (self.mano_inicial + i) % len(self.jugadores)
            orden.append(self.jugadores[indice])

        for jugador in orden:
            if self.mazo:
                carta = self.mazo.pop()
                jugador.recibir_carta(carta)
            elif self.triunfo:
                # El último jugador recibe la carta de triunfo
                jugador.recibir_carta(self.triunfo)
                self.triunfo = None

    def partida_terminada(self):
        """Retorna True si la partida ha terminado."""
        # La partida termina cuando no hay mazo, no hay triunfo y nadie tiene cartas
        if self.mazo or self.triunfo:
            return False
        return all(len(j.mano) == 0 for j in self.jugadores)

    def obtener_ganador(self):
        """
        Retorna el jugador con más puntos.
        Si hay empate, retorna una lista con los empatados.
        """
        if not self.partida_terminada():
            return None

        max_puntos = max(j.puntos for j in self.jugadores)
        ganadores = [j for j in self.jugadores if j.puntos == max_puntos]

        if len(ganadores) == 1:
            return ganadores[0]
        return ganadores

    def obtener_estado(self):
        """Retorna un diccionario con el estado actual del juego."""
        return {
            'triunfo': self.triunfo,
            'mesa': [(j.nombre, c) for j, c in self.mesa],
            'turno': self.jugador_actual().nombre,
            'cartas_mazo': len(self.mazo) + (1 if self.triunfo else 0),
            'puntuaciones': {j.nombre: j.puntos for j in self.jugadores},
        }
