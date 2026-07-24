import hashlib
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# SHA256 - KCV
# CIFRADO: E(00000000000000000000000000000000, CLAVE A CALCULAR KCV). AES/"CBC"

#SHA256: f946108299307d3f6f7585b96013346d
kcvSha256 = hashlib.sha256()
kcvSha256.update(bytes.fromhex("f946108299307d3f6f7585b96013346d"))
print("KCV-256:", kcvSha256.digest().hex()[0:6])

print("----------------------------------------")
key=bytes.fromhex("f946108299307d3f6f7585b96013346d")
texto_plano = bytes.fromhex("00000000000000000000000000000000")
iv_bytes = bytes.fromhex('00000000000000000000000000000000')
cipher = AES.new(key, AES.MODE_ECB,iv_bytes)
texto_cifrado=cipher.encrypt(texto_plano)
print("KCV AES: ", texto_cifrado.hex()[0:6])
print("----------------------------------------")

