# UNIVERSIDAD NACIONAL DE CÓRDOBA

## FACULTAD DE CIENCIAS EXACTAS, FÍSICAS, Y NATURALES

### CÁTEDRA DE REDES DE COMPUTADORAS

**TRABAJO DE LABORATORIO Nro. 7**

**Alumnos:**

- Tosolini Franco Alberto (45702152)
- Scagliotti Marco (46070301)
- Barbero Giovanna Luz (46509956)
- von Büren Thomas (43136697)
- Prieto Quiroz Franco Manuel (46450221)
- Boyé Facundo (46070306)
- Frenguelli Guillermina (45154313)
- Arias valentin (45734482)

**Profesor:** Ingeniero Santiago Henn
**Comisión:** ICOMP24-03
**Año:** 2026

---

# Desafío final: captura, de-codificación y recuperación de datos en redes de computadoras

## 1) IP, máscara y broadcast

- **IP:** `169.254.9.159`
- **Máscara:** `255.255.0.0`
- **Broadcast:** `169.254.255.255`
- **MAC de broadcast:** `FF:FF:FF:FF:FF:FF`

&nbsp;&nbsp;&nbsp;&nbsp;Nos quedó esa IP (no una del rango del aula) porque el DHCP no se completó a tiempo y Windows asignó una IP automática (APIPA, rango 169.254.0.0/16). El broadcast sale de poner en 1 toda la parte de host: como la máscara es /16, cambiamos los últimos dos octetos por 255.255.

## 2) Captura

&nbsp;&nbsp;&nbsp;&nbsp;Capturamos con Wireshark en la interfaz Wi-Fi durante más de 2 minutos. El mensaje llegó 2 veces, con el mismo contenido las dos veces. Captura adjunta: `captura.pcapng`.

## 3) Estructura del mensaje

&nbsp;&nbsp;&nbsp;&nbsp;La carga útil es JSON, con tres campos:

```json
{"SIZE": "4,4", "PL": "<112 bits>", "CHECK": "<32 bits>"}
```

- **SIZE**: tamaño de la matriz (`filas,columnas`), en caracteres.
- **PL**: los bits de datos.
- **CHECK**: los bits de paridad.

&nbsp;&nbsp;&nbsp;&nbsp;Con `SIZE: 4,4` y 7 bits por carácter, esperamos 4×4×7 = 112 bits — coincide con el largo de `PL`. Lo organizamos en una matriz de 4 filas de 28 bits (fila 0 primero). `CHECK` se divide en los primeros 4 bits (paridad de cada fila) y los 28 restantes (paridad de cada columna), tal cual dice el enunciado: primero filas, después columnas. 4+28=32, coincide con `CHECK`.

## 4) Verificación 

&nbsp;&nbsp;&nbsp;&nbsp;Armamos la matriz y recalculamos la paridad de cada fila y columna contra el `CHECK` recibido.

**Resultado:** fallan las 4 filas (0,1,2,3) y las columnas 6, 10, 14 y 19.

## 5) Corrección

&nbsp;&nbsp;&nbsp;&nbsp;Con 4 filas y 4 columnas falladas hay 4 bits corruptos, uno por fila. El problema: con paridad 2D no se puede saber con certeza qué columna le toca a cada fila (hay 24 combinaciones que cierran igual). Probamos las 24 y una sola dio texto con sentido ("Premio" en leet), así que usamos esa:

| Fila | Columna | Recibido | Corregido |
|---|---|---|---|
| 0 | 6 | 1 | 0 |
| 1 | 10 | 1 | 0 |
| 2 | 14 | 1 | 0 |
| 3 | 19 | 1 | 0 |

## 6) Mensaje decodificado

Archivo corregido: `mensaje_corregido.txt`. Corriendo `decodificar_mensaje.py`:

Pr3m
i0!:
)10-
dIeZ
## 7) (Opcional)

`paridad.py` calcula las paridades pero no las compara con el `CHECK` recibido, esa comparación la hicimos aparte pto 4
## Reflexiones e investigación

