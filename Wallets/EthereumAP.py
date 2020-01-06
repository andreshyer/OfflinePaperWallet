from .PrivateKeyGenerator import NewPrivateKey
from .backends import mnemonic
from binascii import unhexlify, hexlify
from ecdsa import SigningKey, SECP256k1
from codecs import decode
from Crypto.Hash import keccak


class EthereumWallet:

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
        # print("Mnemonic Seed: {}".format(self.readable_seed_for_terminal_app))
        print("MyEther Mnemonic Seed: {}".format('Mnemonic Seed for MyEther coming soon'))
        print("Ethereum Private Key: {}".format(self.printable_pk))
        print("Ethereum Address: {}".format(self.address))

    def __init__(self, string, soft=True):
        # Get Private Key
        private_key = NewPrivateKey(string, soft)
        self.printable_pk = private_key
        self.private_key = unhexlify(private_key.encode('ascii'))

        # Generate Seed
        seed = mnemonic.mn_encode(self.printable_pk)  # TODO Create MyEther Mnemonic Seed
        seed.append(mnemonic.mn_checksum(seed))
        self.seed = seed
        self.readable_seed = self.readable_seed(seed)
        self.readable_seed_for_terminal_app = self.readable_seed_for_terminal_app(seed)

        # Get Public Key
        self.sk = SigningKey.from_string(self.private_key, curve=SECP256k1)
        self.vk = self.sk.verifying_key
        public_key_bytes = hexlify(self.vk.to_string())

        # Get Ethereum Address
        public_key_bytes = decode(public_key_bytes, 'hex')
        k = keccak.new(digest_bits=256)
        k.update(public_key_bytes)
        raw_address = k.hexdigest()
        self.address = "0x" + raw_address[-40:]