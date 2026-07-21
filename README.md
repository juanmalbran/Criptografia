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

- **[Nullsec](https://github.com/juanmalbran/nullsec-siem-elk)** — TLS y verificación de certificados en la integración MISP ↔ ELK sobre VPN cifrada.

---

<div align="center">
  <sub>Parte del portfolio de <a href="https://github.com/juanmalbran">Juan Malbrán · M4LBYTE</a></sub>
</div>
