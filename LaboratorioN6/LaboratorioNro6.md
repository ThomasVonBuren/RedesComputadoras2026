# UNIVERSIDAD NACIONAL DE CÓRDOBA

## FACULTAD DE CIENCIAS EXACTAS, FÍSICAS, Y NATURALES

### CÁTEDRA DE REDES DE COMPUTADORAS

**TRABAJO DE LABORATORIO Nro. 6**

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

# PARTE 1: Taller de armado y verificación de cables Cat5/Cat5e (T568A/B)

## 1) Pasos para crimpar un cable derecho (no cruzado)

&nbsp;&nbsp;&nbsp;&nbsp;Para crimpar un cable derecho pimero elegiremos utilizar la norma T568B la cual es un estandar para la construccion de cables y sigue el siguiente codigo de color de izquierda a derecha:
* PIN 1 BLANCO / NARANJA
* PIN 2 NARANJA
* PIN 3 BLANCO / VERDE
* PIN 4 AZUL
* PIN 5 BLANCO / AZUL
* PIN 6 VERDE
* PIN 7 BLANCO / MARRON
* PIN 8 MARRON

Luego, utilizando unas pinzas crimpadoras cortamos aproximadamente 2 cm de la cubierta exterior del cable con cuidado de no dañar los filamentos internos. Proximamente desenredamos y separamos los 4 pares trenzados alisandolos para facilitar la organizacion. Organizamos segun el codigo de color elegido previamente. Nuevamente con la crimpadora realizamos un corte recto y uniforme dejando suelto aproximadamente 1.5 cm de cable. Insertamos en el RJ45 de manera que cada cable pase por su carril y que lleguen hasta el fondo del conector, proximamente introducimos el conector en la cavidad de la crimpadora y apretamos para que el seguro de plastico fije los cables. Por ultimo, repetimos los pasos desde el otro extremo. 
## 2) Construcción del cable

&nbsp;&nbsp;&nbsp;&nbsp;*[Describir el cable construido por el grupo: longitud, norma utilizada, tipo (derecho), dificultades encontradas.]*

![Texto alternativo](./fotos%20parte1/cable_construccion.jpeg)

*Figura 1: Proceso de armado del cable.*

![Texto alternativo](./fotos%20parte1/cable_terminado.jpeg)

*Figura 2: Cable terminado (ambos extremos).*

---

## 3) Verificación del cable

&nbsp;&nbsp;&nbsp;&nbsp;*[Indicar qué grupo intercambió cables con el nuestro (ver punto 4).]*

**a) Inspección visual**

![Texto alternativo](./fotos%20parte1/inspeccion_1.jpeg)

*Figura 3: Inspección visual del cable del otro grupo — extremo A.*

![Texto alternativo](./fotos%20parte1/inspeccion_2.jpeg)

*Figura 4: Inspección visual del cable del otro grupo — extremo B.*

| Aspecto evaluado | ¿Bien / Mal? | Justificación |
| :--- | :--- | :--- |
| Orden de colores correcto según norma | *[ ]* | *[ ]* |
| Los 8 hilos llegan hasta el fondo del conector | *[ ]* | *[ ]* |
| La cubierta exterior ingresa en el conector (alivio de tensión) | *[ ]* | *[ ]* |
| Longitud de destrenzado (no excesiva) | *[ ]* | *[ ]* |
| Crimpado correcto (contactos hundidos, sin hilos sueltos) | *[ ]* | *[ ]* |
| Estado general del conector y del cable | *[ ]* | *[ ]* |
| Ambos extremos con la misma norma | *[ ]* | *[ ]* |

**b) Verificación eléctrica con tester**

![Texto alternativo](./fotos%20parte1/tester.jpeg)

*Figura 5: Verificación con tester de cables Ethernet.*

| Pin | LED tester (extremo local) | LED tester (extremo remoto) | ¿Continuidad correcta? |
| :--- | :--- | :--- | :--- |
| 1 | *[ ]* | *[ ]* | *[ ]* |
| 2 | *[ ]* | *[ ]* | *[ ]* |
| 3 | *[ ]* | *[ ]* | *[ ]* |
| 4 | *[ ]* | *[ ]* | *[ ]* |
| 5 | *[ ]* | *[ ]* | *[ ]* |
| 6 | *[ ]* | *[ ]* | *[ ]* |
| 7 | *[ ]* | *[ ]* | *[ ]* |
| 8 | *[ ]* | *[ ]* | *[ ]* |

**Conclusión de la verificación:** *[¿El cable es apto? ¿Se detectaron fallas (cortos, abiertos, pares cruzados)? ¿Qué se corregiría?]*

---

## 4) Documentación del intercambio de cables

| Cable verificado | Grupo que lo construyó | Grupo que lo verificó | Resultado visual | Resultado eléctrico |
| :--- | :--- | :--- | :--- | :--- |
| *[Nuestro cable]* | Nuestro grupo | *[Grupo X]* | *[ ]* | *[ ]* |
| *[Cable del grupo X]* | *[Grupo X]* | Nuestro grupo | *[ ]* | *[ ]* |

![Texto alternativo](./fotos%20parte1/intercambio.jpeg)

*Figura 6: Evidencia del proceso técnico de verificación con el otro grupo.*

---

# PARTE 2: Equipamiento físico, verificación y utilización de equipos de red y generación de tráfico

## Levantar y testear una LAN

### 1) Configuración manual de la interfaz de red

**Datos de la computadora utilizada:** *[Pc de Giovanna Barbero / Linux / Ubuntu]*

| Parámetro | Valor configurado |
| :--- | :--- |
| a) Dirección IPv4 | *192.1868.1.110* |
| b) Máscara de subred | *255.255.0.0* |
| c) Default gateway | *8.8.8.8* |

![Texto alternativo](./punto1lan.jpeg)

*Figura 10: Configuración manual de la interfaz de red.*

**d) Justificación de las direcciones elegidas:**

&nbsp;&nbsp;&nbsp;&nbsp;*[¿Por qué elegimos esas direcciones? ¿Pertenecen a un rango privado? ¿Están en la misma subred que las PCs de los otros grupos? ¿Tenía sentido configurar un gateway si no había router en la LAN? ¿Tenían o no sentido para la actividad?]*

---

### 2) Conexión al switch y prueba con ping

&nbsp;&nbsp;&nbsp;&nbsp;*[Indicar grupos que compartieron switch, puertos utilizados y estado de los LEDs.]*

```mermaid
graph TD
    SW["Switch Cisco Catalyst 2950"]
    PC1["PC Grupo A<br/>IP: [ ]"]
    PC2["PC Grupo B<br/>IP: [ ]"]
    PC3["PC Grupo C (opcional)<br/>IP: [ ]"]

    PC1 -- "Fa0/[ ]" --- SW
    PC2 -- "Fa0/[ ]" --- SW
    PC3 -- "Fa0/[ ]" --- SW
```

*Figura 11: Topología de la LAN armada (completar IPs y puertos).*

![Texto alternativo](./fotos%20parte2/ping_lan.png)

*Figura 12: Ping exitoso hacia la PC de otro grupo.*

---

### 3) Receptor y emisor UDP con ncat

**Receptor:**

```
ncat -u -l 5000
```

![Texto alternativo](./fotos%20parte2/ncat_receptor.png)

*Figura 13: Receptor UDP escuchando en el puerto 5000.*

**Emisor:**

```
ncat -u [IP_receptor] 5000
```

![Texto alternativo](./fotos%20parte2/ncat_emisor.png)

*Figura 14: Emisor UDP enviando mensajes.*

---

### 4) Captura de paquetes UDP con Wireshark

![Texto alternativo](./fotos%20parte2/wireshark_udp.png)

*Figura 15: Captura general del tráfico UDP.*

![Texto alternativo](./fotos%20parte2/wireshark_udp_detalle.png)

*Figura 16: Detalle de un datagrama UDP (Ethernet / IPv4 / UDP / Data).*

| Capa | Origen | Destino | Campo relevante |
| :--- | :--- | :--- | :--- |
| **Ethernet II** | *[ ]* | *[ ]* | Type: *[ ]* |
| **IPv4** | *[ ]* | *[ ]* | Protocol: UDP (17) |
| **UDP** | Puerto: *[ ]* | Puerto: 5000 | Length: *[ ]* / Checksum: *[ ]* |
| **Datos** | N/A | N/A | *[Contenido del mensaje]* |

Se adjunta también el .pcapng de la prueba, titulado `[nombre_archivo].pcapng`.

---

### 5) Preguntas

**a) ¿Se observa algún procedimiento de establecimiento de conexión antes de enviar los datos?**

&nbsp;&nbsp;&nbsp;&nbsp;*[Respuesta, con referencia a la captura.]*

**b) ¿Existe algún mecanismo de confirmación de recepción equivalente a los ACK de TCP?**

&nbsp;&nbsp;&nbsp;&nbsp;No. UDP es un protocolo sin conexión y no tiene confirmaciones de recepción. En Wireshark se ve que el emisor manda cada datagrama UDP y el receptor no devuelve ningún paquete de confirmación a nivel de transporte. El encabezado UDP tiene solo 4 campos (puerto origen, puerto destino, longitud y checksum), sin número de secuencia ni de confirmación como los de TCP. Por eso el emisor no sabe si el mensaje llegó, se perdió o se duplicó. Si una aplicación necesita esa garantía, la tiene que implementar ella misma en la capa de aplicación.

**c) ¿Qué ocurre si se envían mensajes mientras el receptor UDP no está ejecutándose?**

&nbsp;&nbsp;&nbsp;&nbsp;*[Respuesta. Indicar si apareció ICMP "Port unreachable" en Wireshark y adjuntar captura.]*

![Texto alternativo](./fotos%20parte2/udp_sin_receptor.png)

*Figura 17: Envío de mensajes UDP sin receptor activo.*

**d) ¿UDP garantiza que los mensajes lleguen en el mismo orden en que fueron enviados?**

&nbsp;&nbsp;&nbsp;&nbsp;No. Cada datagrama UDP es independiente y no lleva número de secuencia, así que el protocolo no puede reordenarlos ni detectar que llegaron en otro orden. Cada datagrama puede seguir un camino distinto por la red y llegar desordenado, duplicado o no llegar. En nuestra prueba, al ser una LAN pequeña con un solo switch, los mensajes probablemente llegaron en orden, pero eso es una consecuencia de la red y no una garantía de UDP. TCP, en cambio, numera los bytes y reordena los segmentos antes de entregarlos a la aplicación.

**e) ¿Qué aplicaciones reales utilizan UDP y por qué?**

&nbsp;&nbsp;&nbsp;&nbsp;*[Respuesta: ejemplos (DNS, VoIP, streaming, juegos online, DHCP, etc.) y justificación.]*

---

## Desarrollar un pequeño servidor

### 1) Directorio de archivos e inicio del servidor HTTP

**Archivos del directorio:**

| Archivo | Tipo |
| :--- | :--- |
| *[ ]* | TXT |
| *[ ]* | PDF |
| *[ ]* | Imagen |

```
python3 -m http.server 8000
```

![Texto alternativo](./fotos%20servidor/servidor_inicio.png)

*Figura 18: Servidor HTTP iniciado en la computadora servidora.*

### 2) Acceso desde el navegador

![Texto alternativo](./fotos%20servidor/navegador_listado.png)

*Figura 19: Listado de archivos visto desde el navegador de la segunda computadora.*

![Texto alternativo](./fotos%20servidor/navegador_descarga.png)

*Figura 20: Descarga de un archivo desde el navegador.*

### 3) Transferencia con curl

```
curl -O http://[IP_servidor]:8000/[archivo]
```

![Texto alternativo](./fotos%20servidor/curl.png)

*Figura 21: Descarga del archivo con curl.*

### 4) Captura de tráfico con Wireshark

![Texto alternativo](./fotos%20servidor/wireshark_http.png)

*Figura 22: Captura general del tráfico generado (handshake TCP, GET, respuesta, cierre).*

![Texto alternativo](./fotos%20servidor/wireshark_http_detalle.png)

*Figura 23: Detalle de la petición `GET` y la respuesta `200 OK`.*

**¿De qué tipo es el tráfico?**

&nbsp;&nbsp;&nbsp;&nbsp;*[Respuesta: protocolo de aplicación (HTTP), transporte (TCP), puerto utilizado, comparación con el tráfico UDP anterior, y si va en texto plano.]*

| Capa | Protocolo | Observación |
| :--- | :--- | :--- |
| Aplicación | HTTP | *[ ]* |
| Transporte | TCP | *[ ]* |
| Red | IPv4 | *[ ]* |
| Enlace | Ethernet II | *[ ]* |

---

## Restauración de la configuración de red

&nbsp;&nbsp;&nbsp;&nbsp;*[Confirmar que la interfaz de red volvió a configurarse para obtener dirección de forma automática (DHCP) y que hay acceso a Internet.]*

![Texto alternativo](./fotos%20servidor/dhcp_restaurado.png)

*Figura 24: Interfaz de red restaurada a configuración automática.*

---

## Conclusiones

&nbsp;&nbsp;&nbsp;&nbsp;*[Conclusiones generales del grupo: qué se aprendió de la capa física (cableado, switch), diferencias observadas entre UDP y TCP en la práctica, dificultades encontradas y cómo se resolvieron.]*
