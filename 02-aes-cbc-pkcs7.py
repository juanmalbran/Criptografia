
   
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Cifrado
textoPlano_bytes = bytes('Vemos que ocurre con diferente padding', 'UTF-8')
#Se puede generar aleatoriamente una clave de 16 bytes.
#clave = get_random_bytes(16)
clave = bytes.fromhex('c936108299307d3f6f7585b96013346d')
iv_bytes = bytes.fromhex('47e6831df094b7a6c0ef1fbe0da96ad3')
cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)
texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='pkcs7'))
#Si se generase de forma automática, por no especificarlo en la llamada, se recuperaría así.
iv_b64 = b64encode(cipher.iv).decode('utf-8')
texto_cifrado_b64 = b64encode(texto_cifrado_bytes).decode('utf-8')

print("vector inicializacion=", iv_b64)
print("texto cifrado=", texto_cifrado_b64)

#Descifrado

iv_desc_bytes = bytes.fromhex("47e6831df094b7a6c0ef1fbe0da96ad3")
texto_cifrado_bytes = b64decode(texto_cifrado_b64)
cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size)
print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))
