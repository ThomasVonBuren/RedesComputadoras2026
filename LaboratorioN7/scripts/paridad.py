#!/usr/bin/env python3
import sys

ruta = sys.argv[1] if len(sys.argv) > 1 else "mensaje.txt"

with open(ruta, encoding="utf-8") as f:
    filas = [linea.strip() for linea in f if linea.strip()]

for fila in filas:
    print(fila, "|" + str(fila.count("1") % 2))
print("-" * (len(filas[0]) + 2))
print("".join(str(sum(fila[j] == "1" for fila in filas) % 2) for j in range(len(filas[0]))))
