#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])

#Desarrollo
# clave_codigo = FE12FF2335BC015F --> David codifica en su codigo esta clave
# clave_fichero_conf = 1E12FD2335BC015F --> Fran trabaja en sistemas distribuidos y sube ficheros.

# Key Manager (Felipe) = E000020000000000 (proceso de disociacion de claves)


m = bytes.fromhex("FE12FF2335BC015F")
k = bytes.fromhex("1E12FD2335BC015F")
print(xor_data(m,k).hex())

#Desarrollo -> Integrado -> Produccion

#Integrado
# clave_codigo = FE12FF2335BC015F (Fijo)
# Key Manager (Felipe) =  AE12FF2235BC015F
# clave_integrado (FRan) = ? FE12FF2335BC015F xor AE12FF2235BC015F = 5000000100000000
m = bytes.fromhex("FE12FF2335BC015F")
k = bytes.fromhex("AE12FF2235BC015F")
print(xor_data(m,k).hex())

#Produccion
# clave_codigo = FE12FF2335BC015F (Fijo)
# Key Manager (Felipe) =  BE12112235BC015F
# clave_prod (FRan) = ? FE12FF2335BC015F xor BE12112235BC015F = 4000EE0100000000
m = bytes.fromhex("FE12FF2335BC015F")
k = bytes.fromhex("BE12112235BC015F")
print(xor_data(m,k).hex())


""" print(xor_data(m,k).hex())

num1=0xAE12FF2235BC015F
num2=0x1E12BC2135BD016D
num3=(hex(num1^num2))
print(num3[2:]) """


