from PrivateKeyGenerator import NewPrivateKey
from binascii import unhexlify, hexlify
from ecdsa import SigningKey, SECP256k1
from codecs import decode
from sha3 import keccak_256


class EthereumWallet:

    def WalletDetails(self):
        print("Ethereum Private Key: {}".format(self.printable_pk))
        print("Ethereum Address: {}".format(self.address))

    def __init__(self, string, soft=True):

        private_key = NewPrivateKey(string, soft)
        self.printable_pk = private_key
        self.private_key = unhexlify(private_key.encode('ascii'))

        self.sk = SigningKey.from_string(self.private_key, curve=SECP256k1)
        self.vk = self.sk.verifying_key
        public_key_bytes = hexlify(self.vk.to_string())

        public_key_bytes = decode(public_key_bytes, 'hex')
        k = keccak_256()
        k.update(public_key_bytes)

        raw_address = k.hexdigest()
        self.address = "0x" + raw_address[-40:]

