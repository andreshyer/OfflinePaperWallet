from .PrivateKeyGenerator import NewPrivateKey
from .backends import mnemonic
from hashlib import new, sha256
from binascii import hexlify, unhexlify
from ecdsa import SigningKey, SECP256k1
from base58 import b58encode


class LitecoinWallet:

        @staticmethod
        def readable_seed(raw_seed):
            words = ""
            for word in raw_seed:
                words = words + " " + word
            return words[1:]

        @staticmethod
        def readable_seed_for_terminal_app(raw_seed):
            counter = 0
            words = ""
            for word in raw_seed:
                words = words + " " + word
                if counter == 9:
                    words = words + '\n'
                    counter = 0
                counter = counter + 1
            return words[1:]

        def WalletDetails(self):
            print("Electrum Mnemonic Seed: {}".format(self.readable_seed_for_terminal_app))
            print("Litecoin Private Key: {}".format(self.printable_pk))
            print("Litecoin Address: {}".format(self.address))

        def __init__(self, string, soft=True):
            # Get Private Key
            private_key = NewPrivateKey(string, soft)
            self.printable_pk = private_key
            self.private_key = unhexlify(private_key.encode('ascii'))

            # Generate Seed
            seed = mnemonic.mn_encode(self.printable_pk)
            seed.append(mnemonic.mn_checksum(seed))
            self.seed = seed
            self.readable_seed = self.readable_seed(seed)
            self.readable_seed_for_terminal_app = self.readable_seed_for_terminal_app(seed)

            # Get Public Key
            self.sk = SigningKey.from_string(self.private_key, curve=SECP256k1)
            self.vk = self.sk.verifying_key
            self.public_key = b"04" + hexlify(self.vk.to_string())

            # Get Litecoin Address
            ripemd160 = new('ripemd160')
            ripemd160.update(sha256(unhexlify(self.public_key)).digest())
            self.hashed_public_key = b"30" + hexlify(ripemd160.digest())
            self.checksum = hexlify(sha256(sha256(unhexlify(self.hashed_public_key)).digest()).digest()[:4])
            self.binary_addr = unhexlify(self.hashed_public_key + self.checksum)
            self.address = b58encode(self.binary_addr)

            self.public_key = str(self.public_key)[2:-1]
            self.address = str(self.address)[2:-1]
