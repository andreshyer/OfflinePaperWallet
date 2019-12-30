from .MoneroAP_backends import ed25519, mnemonic, base58
from .PrivateKeyGenerator import NewPrivateKey
from hashlib import sha256
from binascii import unhexlify, hexlify
from Crypto.Hash import keccak

class MoneroWallet:

    @staticmethod
    def hexStrToInt(h):
        '''Converts a hexidecimal string to an integer.'''
        return int.from_bytes(unhexlify(h), "little")

    @staticmethod
    def intToHexStr(i):
        '''Converts an integer to a hexidecimal string.'''
        return hexlify(i.to_bytes(32, "little")).decode("latin-1")

    def fast_hash(self, s):
        # return Keccak().Keccak((len(s)*4, s), 1088, 512, 0x01, 32*8, False).lower()
        s = unhexlify(s)
        k = sha256()
        k.update(s)
        return k.hexdigest()

    def sc_reduce(self, key):
        return self.intToHexStr(self.hexStrToInt(key) % (2 ** 252 + 27742317777372353535851937790883648493))

    def readable_seed(self, raw_seed):
        i = 1
        words = "\n"
        for word in raw_seed:
            words = words + " " + word
            if i % 10 == 0:
                words = words + "\n"
            i += 1
        return words

    def WalletDetails(self):
        print("Monero Public Address: {}".format(self.address))
        print("Monero Mnemonic Seed: {}".format(self.readable_seed))

    def __init__(self, string, soft=True):
        self.private_key = NewPrivateKey(string, soft)
        seed = mnemonic.mn_encode(self.private_key)
        seed.append(mnemonic.mn_checksum(seed))
        self.readable_seed = self.readable_seed(seed)

        sk = self.sc_reduce(self.private_key)
        self.private_spend_key = sk

        k = keccak.new(digest_bits=256)
        k.update(bytes.fromhex(sk))
        vk = k.hexdigest()
        vk = self.sc_reduce(vk)
        self.private_view_key = vk

        public_spend_key = self.hexStrToInt(self.private_spend_key)
        public_spend_key = hexlify(ed25519.encodepoint(ed25519.scalarmultbase(public_spend_key)))
        self.public_spend_key = public_spend_key.decode('utf-8')

        public_view_key = self.hexStrToInt(self.private_view_key)
        public_view_key = hexlify(ed25519.encodepoint(ed25519.scalarmultbase(public_view_key)))
        self.public_view_key = public_view_key.decode('utf-8')

        data = "12" + self.public_spend_key + self.public_view_key
        k = keccak.new(digest_bits=256)
        k.update(bytes.fromhex(data))
        checksum = k.hexdigest()
        self.address = base58.encode(data + checksum[0:8])