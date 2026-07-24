import hashlib


s = hashlib.sha3_256()
print(s.name)
print(s.digest_size)
s.update(bytes("KeepCoding mola un montón","UTF-8"))
print(s.hexdigest())
