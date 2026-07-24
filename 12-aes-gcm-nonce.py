from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import jks
import os

# AES-GCM --> (Datos Asociados + Datos a cifrar) + key + nonce
#Recuperamos la clave. Instalar el: pip install pyjks 

# Obteniendo el path
path = os.path.dirname(__file__)

keystore = path + "/KeyStoreEjemplo"

ks = jks.KeyStore.load(keystore, "123456")

for alias, sk in ks.secret_keys.items():
    print(sk.alias)
    if sk.alias == "cifrado-sim-chacha20-256":
        key = sk.key
        print("Clave AES:", key.hex())

print("Clave AES 2:", key.hex())

key_bytes=key

texto_gcm_bytes = bytes("Vamos a probar si lo sacais", "utf-8")

#key_bytes  = bytes.fromhex('f926108299317d3f6f7585b96013346f')

nonce_bytes = get_random_bytes(8)
print("Nonce hex=", nonce_bytes.hex())
datos_asociados_bytes = bytes("Id usuario","utf-8")
cifrador = AES.new(key_bytes,AES.MODE_GCM,nonce=nonce_bytes)
cifrador.update(datos_asociados_bytes)
texto_cifrado_bytes,mac_bytes = cifrador.encrypt_and_digest(texto_gcm_bytes)
print("Texto cifrado:", texto_cifrado_bytes.hex())
print("MAC:", mac_bytes.hex())

