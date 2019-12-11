from .PrivateKeyGenerator import NewPrivateKey
from hashlib import new, sha256
from binascii import unhexlify, hexlify
from ecdsa import SigningKey, SECP256k1
from base58 import b58encode


class BitcoinWallet:

        def WalletDetails(self):
            print("Bitcoin Private Key: {}".format(self.printable_pk))
            print("Bitcoin Address: {}".format(self.address))

        def __init__(self, string, soft=True):

            private_key = NewPrivateKey(string, soft)
            self.printable_pk = private_key
            self.private_key = unhexlify(private_key.encode('ascii'))

            self.sk = SigningKey.from_string(self.private_key, curve=SECP256k1)
            self.vk = self.sk.verifying_key
            self.public_key = b"04" + hexlify(self.vk.to_string())

            ripemd160 = new('ripemd160')
            ripemd160.update(sha256(unhexlify(self.public_key)).digest())
            self.hashed_public_key = b"00" + hexlify(ripemd160.digest())
            self.checksum = hexlify(sha256(sha256(unhexlify(self.hashed_public_key)).digest()).digest()[:4])
            self.binary_addr = unhexlify(self.hashed_public_key + self.checksum)
            self.address = b58encode(self.binary_addr)

            self.public_key = str(self.public_key)[2:-1]
            self.address = str(self.address)[2:-1]
