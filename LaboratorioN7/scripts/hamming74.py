#!/usr/bin/env python3
"""
hamming74.py — TP7 Redes de Computadoras, Reflexión 4.

Codifica un string de bits (múltiplo de 4) en bloques de Hamming(7,4):
cada 4 bits de datos (d1 d2 d3 d4) se transmiten junto con 3 bits de
paridad (p1 p2 p3), en las posiciones 1..7 = p1 p2 d1 p3 d2 d3 d4.

p1 cubre las posiciones 1,3,5,7
p2 cubre las posiciones 2,3,6,7
p3 cubre las posiciones 4,5,6,7

Si se corrompe un único bit de una palabra de 7, el síndrome (c1,c2,c3)
calculado en la decodificación da, en binario, la posición exacta (1-7)
del bit erróneo: no hace falta ninguna fila/columna externa ni adivinar
por contexto, el propio código "apunta" dónde está el error.

Uso:
    python hamming74.py encode <archivo_con_bits_multiplo_de_4>
    python hamming74.py decode <archivo_con_bits_multiplo_de_7>
"""
import sys


def encode_nibble(d):
    d1, d2, d3, d4 = d
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4
    return [p1, p2, d1, p3, d2, d3, d4]


def decode_word(word):
    p1, p2, d1, p3, d2, d3, d4 = word
    c1 = p1 ^ d1 ^ d2 ^ d4
    c2 = p2 ^ d1 ^ d3 ^ d4
    c3 = p3 ^ d2 ^ d3 ^ d4
    syndrome = c1 + (c2 << 1) + (c3 << 2)
    corrected = word[:]
    if syndrome != 0:
        corrected[syndrome - 1] ^= 1
    p1, p2, d1, p3, d2, d3, d4 = corrected
    return corrected, [d1, d2, d3, d4], syndrome


def encode_bits(bits):
    assert len(bits) % 4 == 0, "la cantidad de bits debe ser múltiplo de 4"
    out = []
    for i in range(0, len(bits), 4):
        nibble = [int(b) for b in bits[i:i + 4]]
        out.extend(encode_nibble(nibble))
    return "".join(str(b) for b in out)


def decode_bits(bits):
    assert len(bits) % 7 == 0, "la cantidad de bits debe ser múltiplo de 7"
    data = []
    syndromes = []
    for i in range(0, len(bits), 7):
        word = [int(b) for b in bits[i:i + 7]]
        _, nibble, syn = decode_word(word)
        data.extend(nibble)
        syndromes.append(syn)
    return "".join(str(b) for b in data), syndromes


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    modo, ruta = sys.argv[1], sys.argv[2]
    with open(ruta, encoding="utf-8") as f:
        bits = f.read().strip()
    if modo == "encode":
        print(encode_bits(bits))
    elif modo == "decode":
        data, syns = decode_bits(bits)
        print(data)
        errores = [(i, s) for i, s in enumerate(syns) if s != 0]
        if errores:
            print("Bloques con bit corregido (bloque, posición 1-7):", errores, file=sys.stderr)
    else:
        print("Modo inválido, usar 'encode' o 'decode'", file=sys.stderr)
        sys.exit(1)
