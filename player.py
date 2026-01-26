from constants import FUERZA_CARTAS, VALORES_CARTAS


class Jugador:
    """Clase base para jugadores."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []           # Cartas en mano (máx 3)
        self.puntos = 0          # Puntos acumulados
        self.bazas_ganadas = []  # Cartas ganadas

    def recibir_carta(self, carta):
        """Añade una carta a la mano del jugador."""
        self.mano.append(carta)

    def jugar_carta(self, indice):
        """Retira y devuelve la carta en el índice dado."""
        if 0 <= indice < len(self.mano):
            return self.mano.pop(indice)
        return None

    def elegir_carta(self, mesa, palo_triunfo):
        """Método abstracto: elige qué carta jugar."""
        raise NotImplementedError("Las subclases deben implementar elegir_carta")

    def __repr__(self):
        return f"Jugador({self.nombre}, puntos={self.puntos})"


class JugadorHumano(Jugador):
    """Jugador que requiere input externo."""

    def elegir_carta(self, mesa, palo_triunfo):
        """Retorna None - el código externo decide qué carta jugar."""
        return None


class JugadorIA(Jugador):
    """IA básica con estrategia simple."""

    def elegir_carta(self, mesa, palo_triunfo):
        """
        Estrategia de la IA:
        - Si es el primero: jugar carta de poco valor
        - Si puede ganar: jugar la carta más baja que gane
        - Si no puede ganar: descartar carta de menor valor
        - Priorizar ganar bazas con muchos puntos
        """
        if not self.mano:
            return None

        # Si es el primero en jugar
        if not mesa:
            return self._elegir_carta_inicial()

        # Hay cartas en la mesa, analizar si puede ganar
        palo_salida = mesa[0][1].palo
        carta_ganadora, _ = self._encontrar_ganadora(mesa, palo_triunfo)

        # Separar cartas por tipo
        cartas_triunfo = [(i, c) for i, c in enumerate(self.mano) if c.palo == palo_triunfo]
        cartas_palo_salida = [(i, c) for i, c in enumerate(self.mano) if c.palo == palo_salida]
        otras_cartas = [(i, c) for i, c in enumerate(self.mano)
                        if c.palo != palo_triunfo and c.palo != palo_salida]

        # Calcular puntos en la mesa
        puntos_mesa = sum(c.valor() for _, c in mesa)

        # Buscar cartas que pueden ganar
        cartas_ganadoras = []

        # Si la carta ganadora actual es triunfo
        if carta_ganadora.palo == palo_triunfo:
            # Solo puedo ganar con un triunfo mayor
            for i, c in cartas_triunfo:
                if FUERZA_CARTAS[c.numero] > FUERZA_CARTAS[carta_ganadora.numero]:
                    cartas_ganadoras.append((i, c))
        else:
            # Puedo ganar con cualquier triunfo o con carta mayor del palo de salida
            cartas_ganadoras.extend(cartas_triunfo)
            for i, c in cartas_palo_salida:
                if FUERZA_CARTAS[c.numero] > FUERZA_CARTAS[carta_ganadora.numero]:
                    cartas_ganadoras.append((i, c))

        # Si hay cartas ganadoras y vale la pena ganar
        if cartas_ganadoras and puntos_mesa >= 4:
            # Jugar la carta ganadora de menor fuerza (ahorra las buenas)
            cartas_ganadoras.sort(key=lambda x: FUERZA_CARTAS[x[1].numero])
            return cartas_ganadoras[0][0]

        # No puede o no vale la pena ganar: descartar carta de menor valor
        return self._elegir_descarte(otras_cartas, cartas_palo_salida, cartas_triunfo)

    def _elegir_carta_inicial(self):
        """Elige carta para iniciar baza: preferir cartas de bajo valor."""
        mejor_indice = 0
        menor_valor = float('inf')

        for i, carta in enumerate(self.mano):
            valor = carta.valor()
            fuerza = FUERZA_CARTAS[carta.numero]
            # Priorizar bajo valor, y si empatan, menor fuerza
            puntuacion = valor * 100 + fuerza
            if puntuacion < menor_valor:
                menor_valor = puntuacion
                mejor_indice = i

        return mejor_indice

    def _encontrar_ganadora(self, mesa, palo_triunfo):
        """Encuentra la carta ganadora actual en la mesa."""
        palo_salida = mesa[0][1].palo
        ganadora = mesa[0][1]
        jugador_ganador = mesa[0][0]

        for jugador, carta in mesa[1:]:
            if self._carta_gana(carta, ganadora, palo_salida, palo_triunfo):
                ganadora = carta
                jugador_ganador = jugador

        return ganadora, jugador_ganador

    def _carta_gana(self, carta, ganadora, palo_salida, palo_triunfo):
        """Determina si 'carta' gana a 'ganadora'."""
        # Triunfo siempre gana a no-triunfo
        if carta.palo == palo_triunfo and ganadora.palo != palo_triunfo:
            return True
        if ganadora.palo == palo_triunfo and carta.palo != palo_triunfo:
            return False

        # Ambas son triunfo o ninguna es triunfo
        if carta.palo == ganadora.palo:
            return FUERZA_CARTAS[carta.numero] > FUERZA_CARTAS[ganadora.numero]

        # Carta que no es del palo de salida ni triunfo nunca gana
        if carta.palo != palo_salida:
            return False

        return False

    def _elegir_descarte(self, otras, palo_salida, triunfos):
        """Elige la carta de menor valor para descartar."""
        # Preferencia: otras cartas > palo salida > triunfos
        candidatas = otras if otras else (palo_salida if palo_salida else triunfos)

        if not candidatas:
            # No debería pasar, pero por seguridad
            return 0

        # Elegir la de menor valor (y menor fuerza si empatan)
        candidatas.sort(key=lambda x: (x[1].valor(), FUERZA_CARTAS[x[1].numero]))
        return candidatas[0][0]
