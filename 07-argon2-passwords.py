from argon2 import PasswordHasher

ph = PasswordHasher()
hash = ph.hash("123456")
print(hash)  
#Ejemplo de salida
#$argon2id$v=19$m=102400,t=2,p=8$68NzeMUoCqPnqgHaaANSBA$qAjcR1nnt847oSZlzEaL2Q
ph.verify(hash, "123456")