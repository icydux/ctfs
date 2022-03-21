from wincrypto import CryptCreateHash,CryptHashData
from wincrypto.constants import CALG_SHA_256
import binascii
import struct


def brute_force(bb,hash):
	hasher = CryptCreateHash(CALG_SHA_256)
	CryptHashData(hasher,bb)
	if hasher.get_hash_val() == hash :
		return True
	else:
		return False

f = open(".data","r")
data = f.read()
hashes = []
flag = b''

while data:
	hashes.append(data[:64])
	data = data[64:]
del hashes[-1]

for i,hash in enumerate(hashes):
	target_hash = binascii.unhexlify(hash)
	for v in range(0xffff):
		bb = struct.pack("h",v)
		if brute_force(bb,target_hash):
			flag += bb
			break
print (flag)

