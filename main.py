#!/usr/bin/env python3
"""Juego interactivo de la Brisca."""

from game import Brisca
from player import JugadorHumano, JugadorIA


def mostrar_estado(partida, jugador_humano):
    """Muestra el estado actual del juego."""
    print("\n" + "=" * 50)
    print(f"Triunfo: {partida.triunfo or f'({partida.palo_triunfo})'}")
    print(f"Cartas en mazo: {len(partida.mazo) + (1 if partida.triunfo else 0)}")
    print("-" * 50)

    # Mostrar puntuaciones
    for j in partida.jugadores:
        marcador = " <--" if j == partida.jugador_actual() else ""
        print(f"{j.nombre}: {j.puntos} puntos{marcador}")

    print("-" * 50)

    # Mostrar mesa
    if partida.mesa:
        print("Mesa:")
        for jugador, carta in partida.mesa:
            print(f"  {jugador.nombre}: {carta}")
    else:
        print("Mesa: (vacía)")

    print("-" * 50)

    # Mostrar mano del jugador humano
    print(f"Tu mano ({jugador_humano.nombre}):")
    for i, carta in enumerate(jugador_humano.mano):
        print(f"  [{i + 1}] {carta} (valor: {carta.valor()})")


def elegir_carta_humano(jugador, partida):
    """Solicita al jugador humano que elija una carta."""
    while True:
        try:
            opcion = input(f"\n{jugador.nombre}, elige carta (1-{len(jugador.mano)}): ")
            indice = int(opcion) - 1
            if 0 <= indice < len(jugador.mano):
                return indice
            print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Introduce un número válido.")


def jugar_baza(partida, jugador_humano):
    """Juega una baza completa."""
    for _ in range(len(partida.jugadores)):
        jugador = partida.jugador_actual()

        if isinstance(jugador, JugadorHumano):
            mostrar_estado(partida, jugador_humano)
            indice = elegir_carta_humano(jugador, partida)
        else:
            indice = jugador.elegir_carta(partida.mesa, partida.palo_triunfo)
            print(f"\n{jugador.nombre} juega: {jugador.mano[indice]}")

        partida.jugar_carta(jugador, indice)

    # Mostrar resultado de la baza
    print("\n" + "=" * 50)
    print("Cartas jugadas:")
    puntos_baza = 0
    for jugador, carta in partida.mesa:
        print(f"  {jugador.nombre}: {carta}")
        puntos_baza += carta.valor()

    ganador = partida.resolver_baza()
    print(f"\n{ganador.nombre} gana la baza! (+{puntos_baza} puntos)")

    # Robar cartas
    partida.robar_cartas()


def mostrar_resultado_final(partida):
    """Muestra el resultado final de la partida."""
    print("\n" + "=" * 50)
    print("PARTIDA TERMINADA")
    print("=" * 50)

    # Ordenar por puntos
    ranking = sorted(partida.jugadores, key=lambda j: j.puntos, reverse=True)

    print("\nPuntuación final:")
    for i, jugador in enumerate(ranking, 1):
        print(f"  {i}. {jugador.nombre}: {jugador.puntos} puntos")

    ganador = partida.obtener_ganador()
    print()
    if isinstance(ganador, list):
        nombres = ", ".join(g.nombre for g in ganador)
        print(f"EMPATE entre: {nombres}")
    else:
        print(f"GANADOR: {ganador.nombre}!")


def configurar_partida():
    """Configura los jugadores para la partida."""
    print("=" * 50)
    print("BRISCA")
    print("=" * 50)

    nombre = input("\nTu nombre: ").strip() or "Jugador"

    while True:
        try:
            num_oponentes = int(input("Número de oponentes (1-3): "))
            if 1 <= num_oponentes <= 3:
                break
            print("Debe ser entre 1 y 3.")
        except ValueError:
            print("Introduce un número válido.")

    jugadores = [JugadorHumano(nombre)]
    for i in range(num_oponentes):
        jugadores.append(JugadorIA(f"Bot{i + 1}"))

    return jugadores


def main():
    """Función principal del juego."""
    jugadores = configurar_partida()
    jugador_humano = jugadores[0]

    partida = Brisca(jugadores)
    partida.iniciar_partida()

    print(f"\nPartida iniciada con {len(jugadores)} jugadores.")
    print(f"Triunfo: {partida.triunfo}")
    input("\nPulsa Enter para comenzar...")

    while not partida.partida_terminada():
        jugar_baza(partida, jugador_humano)

        if not partida.partida_terminada():
            input("\nPulsa Enter para continuar...")

    mostrar_resultado_final(partida)


if __name__ == "__main__":
    main()
