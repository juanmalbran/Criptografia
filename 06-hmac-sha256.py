from Crypto.Hash import HMAC, SHA256

#HMAC clave y datos --- hmac=17938c1b46db10b099e3d0ccc96b685b82a793481b20a931f6e1df7711b8e785
clave_bytes = bytes.fromhex('f2cd441e49faa56419d7832f0bd99311c1a456d2c3e20c596598377257e03085')
datos = bytes("Son necesarios para autenticar. Tened cuidado en España.", "utf8")
hmac256 = HMAC.new(clave_bytes, msg=datos, digestmod=SHA256)
print(hmac256.hexdigest())

