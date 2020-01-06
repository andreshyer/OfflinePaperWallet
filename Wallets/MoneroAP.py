from .backends import ed25519, mnemonic, base58
from .PrivateKeyGenerator import NewPrivateKey
from hashlib import sha256
from binascii import unhexlify, hexlify
from Crypto.Hash import keccak


class MoneroWallet:

    @staticmethod
    def hexStrToInt(h):
        return int.from_bytes(unhexlify(h), "little")

    @staticmethod
    def intToHexStr(i):
        return hexlify(i.to_bytes(32, "little")).decode("latin-1")

    @staticmethod
    def fast_hash(s):
        s = unhexlify(s)
        k = sha256()
        k.update(s)
        return k.hexdigest()

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

    def sc_reduce(self, key):
        return self.intToHexStr(self.hexStrToInt(key) % (2 ** 252 + 27742317777372353535851937790883648493))

    def WalletDetails(self):
        print("Electrum Mnemonic Seed: {}".format(self.readable_seed_for_terminal_app))
        print("Monero Public Address: {}".format(self.address))
        print("Monero Private View Key: {}".format(self.private_view_key))
        print("Monero Private Spend Key: {}".format(self.private_spend_key))

    def __init__(self, string, soft=True):
        # Get Private Key
        self.private_key = NewPrivateKey(string, soft)

        # Generate Seed
        seed = mnemonic.mn_encode(self.private_key)
        seed.append(mnemonic.mn_checksum(seed))
        self.seed = seed
        self.readable_seed = self.readable_seed(seed)
        self.readable_seed_for_terminal_app = self.readable_seed_for_terminal_app(seed)

        # Get Private Spend Key
        sk = self.sc_reduce(self.private_key)
        self.private_spend_key = sk

        # Get Private View Key
        k = keccak.new(digest_bits=256)
        k.update(bytes.fromhex(sk))
        vk = k.hexdigest()
        vk = self.sc_reduce(vk)
        self.private_view_key = vk

        # Get Public Spend Key
        public_spend_key = self.hexStrToInt(self.private_spend_key)
        public_spend_key = hexlify(ed25519.encodepoint(ed25519.scalarmultbase(public_spend_key)))
        self.public_spend_key = public_spend_key.decode('utf-8')

        # Get Public View Key
        public_view_key = self.hexStrToInt(self.private_view_key)
        public_view_key = hexlify(ed25519.encodepoint(ed25519.scalarmultbase(public_view_key)))
        self.public_view_key = public_view_key.decode('utf-8')

        # Get Monero Address
        data = "12" + self.public_spend_key + self.public_view_key
        k = keccak.new(digest_bits=256)
        k.update(bytes.fromhex(data))
        checksum = k.hexdigest()
        self.address = base58.encode(data + checksum[0:8])