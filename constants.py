VALORES_CARTAS = {
    1: 11,   # As
    3: 10,   # Tres
    12: 4,   # Rey
    11: 3,   # Caballo
    10: 2,   # Sota
    # El resto (2, 4, 5, 6, 7) valen 0
}

# Fuerza de las cartas (para determinar ganador de baza)
FUERZA_CARTAS = {
    1: 10,   # As - el más fuerte
    3: 9,
    12: 8,   # Rey
    11: 7,   # Caballo
    10: 6,   # Sota
    7: 5,
    6: 4,
    5: 3,
    4: 2,
    2: 1,    # Dos - el más débil
}

PALOS = ['oros', 'copas', 'espadas', 'bastos']
NUMEROS = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]  # Sin 8 ni 9
