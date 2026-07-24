import ed25519
import hashlib

#Cargar
privatekey = open("myprivatekey-ed25519","rb").read()

signedKey = ed25519.SigningKey(privatekey)

myhash = hashlib.sha256()
myhash.update(bytes("Firmamos esto con la curva 25519", "utf8"))
msg_hasheado=myhash.digest()

signature = signedKey.sign(msg_hasheado, encoding='hex')

print("Firma Generada (64 bytes):", signature.decode("utf-8"))
