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


**Herramientas y materiales utilizados:**

* Cable Cat5/Cat5e, conectores RJ-45, pinza crimpeadora, pelacables y un tester de cable de red. 

**Orden de colores (norma: T568B):**

| Pin | Color del par (T568B) |
| :--- | :--- |
| 1 | Blanco/Naranja |
| 2 | Naranja |
| 3 | Blanco/Verde |
| 4 | Azul |
| 5 | Blanco/Azul |
| 6 | Verde | 
| 7 | Blanco/Marrón |
| 8 | Marrón |

**Procedimiento paso a paso:**

1. Pelar la cubierta exterior 2-3 cm aprox.
2. Separar y destrenzar los pares.
3. Ordenar los hilos según la norma elegida.
4. Cortar a ras y emparejar los hilos.
5. Insertar en el conector RJ-45, verificar que lleguen al fondo.
6. Apretar el conector.
7. Repetir en el otro extremo con la misma norma.

*Fuente(s) consultada(s): [videos / tutoriales utilizados]*

---

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

| Cable verificado | Grupo que lo construyó | Grupo que lo verificó | Resultado visual | Resultado eléctrico |
| :--- | :--- | :--- | :--- | :--- |
| *[Nuestro cable]* | Nuestro grupo | *[Grupo X]* | *[ ]* | *[ ]* |
| *[Cable del grupo X]* | *[Grupo X]* | Nuestro grupo | *[ ]* | *[ ]* |

![Texto alternativo](./fotos%20parte1/intercambio.jpeg)

*Figura 6: Evidencia del proceso técnico de verificación con el otro grupo.*

---

# PARTE 2: Equipamiento físico, verificación y utilización de equipos de red y generación de tráfico

## Opcional

### 1) Características principales del switch Cisco Catalyst 2950

*[Resumen basado en el datasheet: cantidad y velocidad de puertos, capacidad de conmutación, tabla MAC, soporte de VLANs, puerto consola, etc.]*

| Característica | Valor |
| :--- | :--- |
| Modelo | Cisco Catalyst 2950 Series |
| Puertos | *[ ]* |
| Velocidad de los puertos | *[ ]* |
| Capacidad de conmutación | *[ ]* |
| Tamaño de tabla MAC | *[ ]* |
| Otras | *[ ]* |

![Texto alternativo](./fotos%20parte2/switch_frontal.jpeg)

*Figura 7: Panel frontal del switch (indicadores y puertos).*

![Texto alternativo](./fotos%20parte2/switch_trasero.jpeg)

*Figura 8: Panel trasero del switch (alimentación, puerto de consola).*

### 2) Checklists de procedimientos

**a) Conexión a la consola del switch (PuTTY, 9600 baudios)**

- [ ] *[Conectar cable serie/RJ-45 al puerto consola del switch.]*
- [ ] *[Conectar el adaptador serie-USB a la PC e identificar el puerto COM en el Administrador de dispositivos.]*
- [ ] *[Abrir PuTTY → Serial → COMx → Speed: 9600.]*
- [ ] *[Verificar acceso al prompt del switch.]*

![Texto alternativo](./fotos%20parte2/putty.png)

*Figura 9: Acceso a la consola del switch mediante PuTTY.*

**b) Administración del switch y habilitación de interfaces**

- [ ] *[enable]*
- [ ] *[configure terminal]*
- [ ] *[interface fastEthernet 0/X]*
- [ ] *[no shutdown]*
- [ ] *[end / show interfaces status]*

```
(Pegar aquí la salida de consola relevante)
```

---

## Levantar y testear una LAN

### 1) Configuración manual de la interfaz de red

**Datos de la computadora utilizada:** *[Nombre / SO / interfaz]*

| Parámetro | Valor configurado |
| :--- | :--- |
| a) Dirección IPv4 | *[ ]* |
| b) Máscara de subred | *[ ]* |
| c) Default gateway | *[ ]* |

![Texto alternativo](./fotos%20parte2/config_ip.png)

*Figura 10: Configuración manual de la interfaz de red.*

**d) Justificación de las direcciones elegidas:**

&nbsp;&nbsp;&nbsp;&nbsp;*[¿Por qué elegimos esas direcciones? ¿Pertenecen a un rango privado? ¿Están en la misma subred que las PCs de los otros grupos? ¿Tenía sentido configurar un gateway si no había router en la LAN? ¿Tenían o no sentido para la actividad?]*

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

&nbsp;&nbsp;&nbsp;&nbsp; No, en este protocolo (UDP) no se posee ningún mecanismo de confirmación del estilo ACK, el mismo es un protocolo no orientado a la conexión y no confiable, es decir, envia la información sin confirmar que fue recibida o si se produjo algun conflicto en el camino.

**c) ¿Qué ocurre si se envían mensajes mientras el receptor UDP no está ejecutándose?**

&nbsp;&nbsp;&nbsp;&nbsp;*[Respuesta. Indicar si apareció ICMP "Port unreachable" en Wireshark y adjuntar captura.]*

![Texto alternativo](./fotos%20parte2/udp_sin_receptor.png)

*Figura 17: Envío de mensajes UDP sin receptor activo.*

**d) ¿UDP garantiza que los mensajes lleguen en el mismo orden en que fueron enviados?**

&nbsp;&nbsp;&nbsp;&nbsp;No, UDP no garantiza que los mensajes lleguen en el mismo orden en que fueron enviados. Cada transmisión se trata de forma independiente, como cada paquete puede seguir una ruta diferente dentro de la red, no existe garantía de que lleguen ordenados, que no se dupliquen o incluso de que lleguen a destino. Además, la cabecera de UDP no incluye números de secuencia para que el receptor pueda reordenarlos.
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
