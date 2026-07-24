from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256
import secrets

salt = bytes.fromhex("1994091fa58d0545663225ea86ff632f") #Mi identificador
master_secret = bytes.fromhex("d32de7cce8cd745fb92558e552c0497c39dd1ea79df58f887b1d1fe79fee7637") #Mi clave maestra
key1, key2 = HKDF(master_secret, 32, salt, SHA256, 2)

print("Clave key1: ", key1.hex()) # Clave de cifrado
print("Clave key2: ", key2.hex()) # Clave de MAC