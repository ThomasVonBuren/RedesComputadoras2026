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
* 1) ¿Qué hubiera pasado si el mensaje tenía errores en dos bits de filas y columnas distintas? ¿Y si se dañaba un bit
de los de control?
    
   Si se alteran dos bits en filas y columnas distintas, la paridad bidimensional detecta el problema porque fallan las paridades de dos filas y dos columnas. Sin embargo, no permite identificar de manera única los bits afectados, ya que existen dos emparejamientos posibles entre esas filas y columnas.
   Si se altera únicamente un bit de CHECK, aparece una discrepancia en la verificación correspondiente. Bajo la hipótesis de un único error en todo el bloque, una discrepancia aislada permite identificar el bit de control dañado; un error en los datos produciría una discrepancia de fila y otra de columna.

* 2) Si el mensaje es texto en castellano, muchas veces un error "se adivina" por contexto(Hola mondo). ¿Sirve eso para una contraseña, un número de cuenta o una dirección web? ¿Qué aporta el código frente a "leer y adivinar"?

    El contexto puede ayudar a interpretar una palabra, pero no permite recuperar de forma confiable una contraseña, un número de cuenta o una dirección web: un carácter diferente podría dar lugar a otro valor válido.

    El código aporta una verificación matemática independiente del significado del mensaje. Permite detectar o corregir errores dentro de sus capacidades, pero no garantiza una recuperación perfecta ante cualquier patrón de alteraciones.

* 3) ¿Confirmaron que la corrección es correcta? 

Solo en parte. Confirmamos que es consistente: cierran todas las paridades y el texto tiene sentido. Pero eso no prueba que sea la única corrección válida, las otras 23 combinaciones también cerraban la paridad igual de bien. La elegimos por el contenido, no porque la matemática la señalara como la única opción.

* 4) Hamming (7,4)

Hamming (7,4) agrega tres bits de paridad a cada cuatro bits de datos y forma palabras de siete bits con la distribución p1 p2 d1 p3 d2 d3 d4. Para paridad par:

- p1 = d1 XOR d2 XOR d4, verificando las posiciones 1, 3, 5 y 7.
- p2 = d1 XOR d3 XOR d4, verificando las posiciones 2, 3, 6 y 7.
- p3 = d2 XOR d3 XOR d4, verificando las posiciones 4, 5, 6 y 7.

Al recibir una palabra se calculan los chequeos s1, s2 y s3. El síndrome, interpretado como el número binario s3 s2 s1, indica la posición del bit alterado cuando ocurrió un único error. Si vale cero, no se detectan errores.

Hamming (7,4) garantiza corregir un error por palabra de siete bits. Si se alteran varios bits dentro de una misma palabra, puede producir una corrección incorrecta. Por eso, su ventaja depende del patrón de errores y no implica que sea superior en todos los casos a la paridad bidimensional.

Agrega tres bits de control por cada cuatro de datos, un 75 % respecto de los datos originales, frente al aproximadamente 29 % de nuestro esquema.

Aplicamos Hamming (7,4) a los 112 bits corregidos mediante scripts/hamming74.py, generando un paquete de 196 bits en data/paquete_hamming.bits. En la prueba realizada, alteramos un bit y el decodificador lo detectó y corrigió mediante el síndrome.