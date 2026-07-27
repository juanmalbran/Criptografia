<h1 align="center">Criptografía</h1>

<p align="center">
  <img src="https://img.shields.io/badge/AES-005571?style=flat-square" />
  <img src="https://img.shields.io/badge/RSA-BC8CFF?style=flat-square" />
  <img src="https://img.shields.io/badge/GPG%2FPGP-0093DD?style=flat-square&logo=gnuprivacyguard&logoColor=white" />
  <img src="https://img.shields.io/badge/TLS%2FPKI-3FB950?style=flat-square" />
</p>

---

## Sobre este módulo

Los fundamentos matemáticos que sostienen la confidencialidad, la integridad y la autenticación de la información. Del cifrado clásico a la criptografía moderna, con foco en **entender los conceptos, no reinventarlos** (nunca implementes tu propia criptografía).

**Temas cubiertos:** cifrado simétrico y asimétrico · cifrado de bloque y de flujo · funciones de hash · MAC/HMAC · firmas digitales · RSA, Diffie-Hellman, ECC · PKI · TLS/SSH/VPN · esteganografía · criptografía post-cuántica.

---

## 📄 Práctica final — 15 ejercicios resueltos

> **[Ver informe completo (PDF)](Criptografia_Practica_Final_Juan_Malbran.pdf)** — resolución paso a paso de los 15 ejercicios, con procedimiento, herramientas y resultados.

La práctica recorre la criptografía aplicada de punta a punta; cada ejercicio parte de un caso concreto:

| # | Ejercicio | Concepto |
|---|---|---|
| 1 | Derivación de clave por XOR | Disociar la clave del código: clave fija + dinámica combinadas en memoria, distinta por entorno |
| 2 | Descifrado AES-CBC | Bloque de 128 bits, IV de ceros, padding PKCS7 |
| 3 | Migración ChaCha20 → ChaCha20-Poly1305 | Pasar de solo cifrado a AEAD (confidencialidad + integridad + autenticidad) |
| 4 | Análisis de un JWT | Header / Payload / Firma: por qué sin la clave no se puede falsificar el rol (`isAdmin`) |
| 5 | Hashing SHA-3 / Keccak | Deducir el tamaño (SHA3-256 vs SHA2-512) por la longitud del hash; efecto avalancha |
| 6 | HMAC-SHA256 | Autenticación de mensaje con clave del keystore |
| 7 | Almacenamiento de contraseñas | Por qué SHA-1 no sirve; añadir SALT y luego PEPPER |
| 8 | API REST sin TLS | Elegir un esquema AEAD (AES-GCM vs ChaCha20-Poly1305) para proteger el contenido, no el canal |
| 9 | KCV de una clave AES | Key Check Value por dos vías: SHA-256 y AES-CBC (primeros 3 bytes) |
| 10 | Firma y cifrado PGP | Kleopatra: verificar con clave pública, firmar y cifrar con clave privada |
| 11 | RSA-OAEP con SHA-256 | Descifrar la clave simétrica con la privada; por qué el recifrado cambia (aleatoriedad) |
| 12 | AES-GCM y reutilización de nonce | El fallo de reusar nonce + clave; solución con nonce aleatorio |
| 13 | Firmas digitales RSA (PKCS#1 v1.5) y Ed25519 | Dos firmas sobre el mismo mensaje: RSA vs curva elíptica |
| 14 | Derivación HKDF-SHA512 | Derivar una clave AES-256 usando el device ID como salt |
| 15 | Key Block TR-31 | Importar/desenvolver una clave protegida sin que viaje en claro (librería `psec`) |

---

## Concepto clave — Simétrico vs Asimétrico

La distinción que más se confunde: una sola clave compartida frente a un par de claves pública/privada. El cifrado híbrido (TLS) combina ambos: asimétrico para intercambiar la clave, simétrico para los datos.

![Cifrado simétrico vs asimétrico](cifrado-simetrico-asimetrico.png)

---

## Temas destacados

- **Principios** — Kerckhoff (solo la clave es secreta), evitar complejidad innecesaria, usar librerías probadas.
- **Práctica con GPG/PGP** — generación y gestión de claves, cifrado/descifrado, firma y verificación de mensajes.
- **Esteganografía** — ocultar información en imágenes (LSB), a diferencia del cifrado que oculta el contenido pero no su existencia.
- **Almacenamiento seguro** — hashing de contraseñas, KDFs, JWT.

---

## Stack

`OpenSSL` · `GPG` · `PyCryptodome` · `hashcat` · `steghide`

---

## Módulo relacionado

- **[Nullsec](https://github.com/juanmalbran/Nullsec-SIEM-ELK)** — TLS y verificación de certificados en la integración MISP ↔ ELK sobre VPN cifrada.

---

<div align="center">
  <sub>Parte del portfolio de <a href="https://github.com/juanmalbran">Juan Malbrán · M4LBYTE</a></sub>
</div>
