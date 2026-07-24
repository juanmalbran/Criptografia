from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import os

#Cargamos la clave PRIVADA porque generamos una firma
my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "/claveprivada-RSA_desc_oaep.pem"
keypriv = RSA.importKey(open(path_file_priv).read())

mensaje_bytes = bytes("Podemos firmar cualquier longitud de datos porque previamente lo hasheamos","utf-8")
hash = SHA256.new(mensaje_bytes)

firmador=PKCS115_SigScheme(keypriv) ## Generamos un Signer 
firma = firmador.sign(hash)
print("Firma: ", firma.hex())
