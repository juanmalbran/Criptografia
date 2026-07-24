from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import os


#RSA OAEP Bueno para cifrar. 
#Proceso de carga firma
my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "/claveprivada-RSA_desc_oaep.pem"
keypriv = RSA.importKey(open(path_file_priv).read())



MensajeCifrado = bytes.fromhex("1b2836a466ded179de693a3dfea3f25b880589b68926a340530898d3a47ac46bf05b499cea0fad476c9b085ed286226b0fc674bc772dd9064f95d302ce8b0fa50ccbb6517c36cc5dc89b192377338bb478a08ffb1511d26c3a4c9e7a852cef037b93edf82bd51b7cb778b6e3c06eed64574bd72dc0bee2e41937f17f2de82c4aa88b3d3bfd73bc35b57427bdd76ca4d666472a18840e15db75e85bc950df05976c6a0f6e9a50daaee85788bf4d31d6ed024416d20af644968ba37a4a748942c0fe1ee692e22910e4a49380efe47754d6f61328335c6228b2002b189580bffe37f3c332aa435cf564b6c41a6d6353b0b6e675c79cc427fc49689c35cb686bc346")

decryptor = PKCS1_OAEP.new(keypriv,SHA256)
decrypted = decryptor.decrypt(MensajeCifrado)

print("Cifrado:", decrypted.hex())
print("--------------------------------------------------")