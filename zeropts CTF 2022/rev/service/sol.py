from wincrypto import CryptCreateHash,CryptHashData
from wincrypto.constants import CALG_SHA_256
import binascii
import struct

flag = b''

def brute_force(possible,hash):
	hasher = CryptCreateHash(CALG_SHA_256)
	CryptHashData(hasher,possible)
	if hasher.get_hash_val() == hash :
		return True
	else:
		return False

f = open(".data","r")
data = f.read()
hashes = []

while data:
	hashes.append(data[:64])
	data = data[64:]
del hashes[-1]

for i,hash in enumerate(hashes):
	target = binascii.unhexlify(hash)
	for v in range(0xffff):
		possible = struct.pack("h",v)
		if brute_force(possible,target):
			flag += possible
			break
print (flag)

