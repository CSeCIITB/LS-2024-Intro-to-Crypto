from Crypto.Cipher import AES
from Crypto.Util.number import getPrime, long_to_bytes
from Crypto.Random import random
from Crypto.Random.random import randrange
from Crypto.Random.random import getrandbits
flag = b"[REDACTED_FLAG]"
p = getPrime(2048)
g = random.randrange(1,p)
a = random.randrange(1,p)
b = random.randrange(1,p)
A = (g*a)%p
B = (g*b)%p
key = long_to_bytes(((B*a)%p)%pow(2,16*8))
iv=long_to_bytes(getrandbits(16*8))
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
ct = cipher.encrypt(flag).hex()
print(p, g, A, B, ct, iv.hex())
