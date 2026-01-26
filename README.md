# Brisca

Juego de cartas de la Brisca implementado en Python para 2-4 jugadores.

## Requisitos

- Python 3.6+

## Instalacion

```bash
git clone https://github.com/ziobermeo-code/brisca.git
cd brisca
```

## Uso

```bash
python3 main.py
```

El juego te pedira tu nombre y el numero de oponentes (1-3 bots).

## Reglas del juego

### Objetivo
Conseguir el mayor numero de puntos capturando cartas de valor.

### Puntuacion de cartas
| Carta | Puntos |
|-------|--------|
| As | 11 |
| 3 | 10 |
| Rey | 4 |
| Caballo | 3 |
| Sota | 2 |
| 7, 6, 5, 4, 2 | 0 |

**Total:** 120 puntos en el mazo.

### Fuerza de las cartas (de mayor a menor)
```
As > 3 > Rey > Caballo > Sota > 7 > 6 > 5 > 4 > 2
```

### Flujo del juego
1. Se reparten 3 cartas a cada jugador
2. Se descubre una carta que define el palo de triunfo
3. Por turnos, cada jugador juega una carta
4. Gana la baza:
   - La carta de triunfo mas alta, o
   - La carta mas alta del palo de salida (si no hay triunfos)
5. El ganador recoge las cartas y suma sus puntos
6. Los jugadores roban del mazo (el ganador primero)
7. Cuando se acaba el mazo, se juegan las ultimas bazas
8. Gana quien tenga mas puntos

## Estructura del proyecto

```
brisca/
├── constants.py   # Valores y fuerza de las cartas
├── deck.py        # Clase Carta y funciones del mazo
├── player.py      # Clases Jugador, JugadorHumano, JugadorIA
├── game.py        # Motor del juego (clase Brisca)
└── main.py        # Interfaz interactiva por terminal
```

## Ejemplo de partida

```
$ python3 main.py
==================================================
BRISCA
==================================================

Tu nombre: Ana
Numero de oponentes (1-3): 1

Partida iniciada con 2 jugadores.
Triunfo: 3 de espadas

Tu mano (Ana):
  [1] 5 de copas (valor: 0)
  [2] Rey de oros (valor: 4)
  [3] As de bastos (valor: 11)

Ana, elige carta (1-3):
```

## Licencia

MIT
