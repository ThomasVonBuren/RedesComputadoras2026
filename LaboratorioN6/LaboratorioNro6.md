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
**Procedimiento de armado (Norma T568B)**

Para la construcción del cable de red directo, se seleccionó la norma **T568B** en ambos extremos del cable. El procedimiento consistió en los siguientes pasos:

1. **Deschaquetado:** Se retiraron aproximadamente 2 cm de la cubierta exterior de PVC del cable UTP sin dañar el aislamiento de los pares trenzados internos.
2. **Destrenzado y ordenamiento:** Se destrenzaron los pares y se ordenaron según el código de colores de la norma elegida:
   * **T568B:** Blanco/Naranja, Naranja, Blanco/Verde, Azul, Blanco/Azul, Verde, Blanco/Marrón, Marrón.
3. **Alineación y corte:** Se alinearon los hilos en un mismo plano, rectificándolos y recortándolos en línea recta a aproximadamente 1.2 cm para asegurar que ingresen parejos al conector.
4. **Inserción y crimpado:** Se introdujeron los hilos firmemente dentro del conector RJ-45 asegurando que cada conductor llegara hasta el fondo de su canal correspondiente y que la cubierta exterior quedara dentro de la lengüeta de retención del conector. Se utilizó la pinza crimpeadora para fijar los contactos metálicos y el sujetador de la chaqueta.

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

* **Longitud:** Aproximadamente 1,5 metros.
* **Norma utilizada:** T568B en ambos extremos.
* **Tipo de cable:** Cable de parcheo directo (patch cord / no cruzado).
* **Dificultades encontradas:** Al momento de ordenar los pares de hilos, algunos conductores tendían a entrelazarse o cruzarse de posición al insertarlos dentro del conector. 

<img width="1600" height="900" alt="b87b2242-f019-4155-9d86-28a6082a8618" src="https://github.com/user-attachments/assets/5fbf3aa8-2a90-4200-9816-290cc8f9e859" />

Figura 1: Cable terminado (ambos extremos).

---

## 3) Verificación del cable

Los cables que verificamos son del grupo MacacOS.

**a) Inspección visual**

<img width="1200" height="1600" alt="dfd10adf-bba6-4403-b463-3600678c3f90" src="https://github.com/user-attachments/assets/659d4d7a-4982-4107-a45e-b0249f566366" />


*Figura 2: Inspección visual del cable del otro grupo — extremo A.*

<img width="1200" height="1600" alt="599584be-0097-4c97-bf57-edd9025d3043" src="https://github.com/user-attachments/assets/a22a9263-2e84-4354-bca1-42ad133c53a0" />


*Figura 3: Inspección visual del cable del otro grupo — extremo B.*

| Aspecto evaluado | ¿Bien / Mal? | Justificación |
| :--- | :--- | :--- |
| Orden de colores correcto según norma | *Bien* | *Segun la norma T568B, el orden de los colores es el correcto* |
| Los 8 hilos llegan hasta el fondo del conector | *Bien* | *Se podia apreciar como los 8 hilos llegaban hacia el fondo* |
| La cubierta exterior ingresa en el conector (alivio de tensión) | *Mal* | *En un extremo se ve como la cubierta exterior ingresa, pero en otro extremo se nota como no * |
| Longitud de destrenzado (no excesiva) | *Bien* | *La longitud de destrenzado era la adecuada* |
| Crimpado correcto | *Bien* | *En la verificacion, se podia apreciar contactos hundidos y no se vio ningun hilo suelto* |
| Estado general del conector y del cable | *Bien* | *El conector parecia firme, y el cable no parecia estar en mal estado. El cable paso la verificacion por tester* |
| Ambos extremos con la misma norma | *Si* | *La norma que utilizaron fue: T568B* |

**b) Verificación eléctrica con tester**

![Texto alternativo](./imagenes/punto%203b.jpeg)

*Figura 5: Verificación con tester de cables Ethernet.*

En esta imagen se verifica como el primer cable esta armado de forma correcta, asi como se ve en esta imagen se ven el testeo con los demas cables. 

| Pin | LED tester (extremo local) | LED tester (extremo remoto) | ¿Continuidad correcta? |
| :--- | :--- | :--- | :--- |
| 1 | *Encendido* | *Encendido* | *Correcto* |
| 2 | *Encendido* | *Encendido* | *Correcto* |
| 3 | *Encendido* | *Encendido* | *Correcto* |
| 4 | *Encendido* | *Encendido* | *Correcto* |
| 5 | *Encendido* | *Encendido* | *Correcto* |
| 6 | *Encendido* | *Encendido* | *Correcto* |
| 7 | *Encendido* | *Encendido* | *Correcto* |
| 8 | *Encendido* | *Encendido* | *Correcto* |

**Conclusión de la verificación:** *El cable que intercambiamos resulto ser apto, no se detecto ningun tipo de falla y el testeo del mismo resulto correcto.*

---

## 4) Documentación del intercambio de cables

El intercambio de cables se realizó con MacacOS. Recibimos el cable construido por el otro para realizar la inspección visual y la prueba eléctrica con tester, según el procedimiento descrito en los incisos 3a y 3b. Ambos cables obtuvieron resultados positivos.

![Detalle del conector del cable intercambiado](./fotos%20parte1/intercambio_1.jpeg)

*Figura 6a: Detalle del conector del cable intercambiado.*

![Vista de la terminación del cable](./fotos%20parte1/intercambio_2.jpeg)

*Figura 6b: Vista de la terminación del cable.*

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

Se utilizó la dirección privada 192.168.1.110 con máscara 255.255.0.0 (/16). Esta configuración ubica al equipo en la misma subred que 192.168.1.10, permitiendo la comunicación local mediante el switch.
No era necesario configurar un gateway porque no se necesitaba acceder a otras redes. El valor 8.8.8.8 que aparece en una captura corresponde a un servidor DNS público y no era adecuado como puerta de enlace.

---

### 2) Conexión al switch y prueba con ping

Conectamos los cables que armamos a un switch y mandamos el ping a la IP del grupo con el cual realizamos esta parte.

![Texto alternativo](./imagenes/punto%202.jpeg)

*Figura 11: Ping exitoso hacia la PC de otro grupo.*

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

<img width="1366" height="768" alt="9d12b745-9759-4f96-8ca4-1dd777b360ba" src="https://github.com/user-attachments/assets/daa7bce6-b239-4a23-98e3-6f2882a2e9ab" />



*Figura 15: Captura general del tráfico UDP.*


| Capa | Origen | Destino | Campo relevante |
| :--- | :--- | :--- | :--- |
| **Ethernet II** | *b0:66:80 (f4:39:09:b0:66:80)* | *00:22:70:68:00:00* | Type: *IPv4 (0x0800)* |
| **IPv4** | *192.168.1.10* | *192.168.1.110* | Protocol: UDP (17) |
| **UDP** | Puerto: *50179* | Puerto: 5000 | Length: *14*  |
| **Datos** | N/A | N/A | *hola\n (6 bytes)* |

Se adjunta también el .pcapng de la prueba, titulado `[nombre_archivo].pcapng`.

---

### 5) Preguntas

**a) ¿Se observa algún procedimiento de establecimiento de conexión antes de enviar los datos?**

&nbsp;&nbsp;&nbsp;&nbsp;*[Respuesta, con referencia a la captura.]*

**b) ¿Existe algún mecanismo de confirmación de recepción equivalente a los ACK de TCP?**

&nbsp;&nbsp;&nbsp;&nbsp;No. UDP es un protocolo sin conexión y no tiene confirmaciones de recepción. En Wireshark se ve que el emisor manda cada datagrama UDP y el receptor no devuelve ningún paquete de confirmación a nivel de transporte. El encabezado UDP tiene solo 4 campos (puerto origen, puerto destino, longitud y checksum), sin número de secuencia ni de confirmación como los de TCP. Por eso el emisor no sabe si el mensaje llegó, se perdió o se duplicó. Si una aplicación necesita esa garantía, la tiene que implementar ella misma en la capa de aplicación.

**c) ¿Qué ocurre si se envían mensajes mientras el receptor UDP no está ejecutándose?**

Si el receptor UDP no está ejecutándose, los mensajes enviados a ese puerto no quedan en espera para cuando se inicie: se descartan. El equipo destino puede responder con un mensaje ICMP “Port Unreachable”, aunque esto depende de su configuración y del firewall. UDP no garantiza la entrega ni retransmite los mensajes perdidos.

**d) ¿UDP garantiza que los mensajes lleguen en el mismo orden en que fueron enviados?**

&nbsp;&nbsp;&nbsp;&nbsp;No. Cada datagrama UDP es independiente y no lleva número de secuencia, así que el protocolo no puede reordenarlos ni detectar que llegaron en otro orden. Cada datagrama puede seguir un camino distinto por la red y llegar desordenado, duplicado o no llegar. En nuestra prueba, al ser una LAN pequeña con un solo switch, los mensajes probablemente llegaron en orden, pero eso es una consecuencia de la red y no una garantía de UDP. TCP, en cambio, numera los bytes y reordena los segmentos antes de entregarlos a la aplicación.

**e) ¿Qué aplicaciones reales utilizan UDP y por qué?**

&nbsp;&nbsp;&nbsp;&nbsp;UDP se usa en aplicaciones donde importan más la baja latencia y la simplicidad que la entrega garantizada de cada paquete. Como es un protocolo sin conexión, no necesita handshake, no espera confirmaciones y no retransmite, por lo que tiene menos demora y menos sobrecarga que TCP. Por eso lo usan servicios como DNS, donde las consultas son mensajes cortos de pregunta y respuesta y, si no llega respuesta, el cliente simplemente repite la consulta, y DHCP, donde el cliente todavía no tiene dirección IP y no podría establecer una conexión TCP, por lo que pide su configuración con mensajes en broadcast. También lo usan las aplicaciones en tiempo real, como VoIP, videollamadas, streaming en vivo y juegos online, porque en ellas es preferible perder un fragmento de audio, video o un dato de posición que esperar una retransmisión que llegaría tarde y ya no serviría. Por último, protocolos como NTP (sincronización de hora) y QUIC/HTTP/3 también funcionan sobre UDP. QUIC implementa por su cuenta la fiabilidad y el control de congestión en la capa de aplicación, con menos latencia de conexión que TCP. En conclusión, UDP conviene cuando la aplicación tolera pérdidas o resuelve la fiabilidad por sí misma, a diferencia de la transferencia de archivos o la navegación web clásica, que necesitan que todos los datos lleguen completos y en orden y por eso usan TCP.

---
## Conclusiones

&nbsp;&nbsp;&nbsp;&nbsp;Luego de pasar por este trabajo y experimentar como podemos generar y levantar nuestrar propias conexiones entre computadoras, podemos afirmar que logramos adquirir grandes habilidades que seran muy utiles en el ambito profesional y hasta inclusive personal, nos parecio muy interesante el proceso de crimpear un cable para poder usarlo para las conexiones y sin lugar a duda ahora estamos mas capacitados e interiorizados para trabajar con redes de computadoras.