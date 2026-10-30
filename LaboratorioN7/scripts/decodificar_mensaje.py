#!/usr/bin/env python3
import sys

ruta = sys.argv[1] if len(sys.argv) > 1 else "mensaje.txt"

with open(ruta, encoding="utf-8") as f:
    for linea in f:
        bits = linea.strip()
        if bits:
            print("".join(chr(int(bits[k:k + 7], 2)) for k in range(0, len(bits), 7)))
