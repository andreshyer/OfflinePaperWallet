from datetime import datetime
from hashlib import sha3_256
from secrets import randbelow

'''
This is the core of the cryptography of this code, each wallet is backed by a private key. It is CRITICAL that no one
knows your private key. Your private key is derived from the passphrase that you enter using the SHA256 protocol.
Make sure you use a strong passphrase, as you do not want others to be able to reproduce your key. Even if you the
'non-recoverable' mode, it is strongly advised you use a long passphrase so others can no reverse engineer your private
key. Although this code is simple, it is important to ensuring that each of the wallets in this application are secure. 
'''

def NewPrivateKey(string, soft):
    if soft:
        return sha3_256(string.encode('utf-8')).hexdigest()  # Return output for string digested as sha_256

    time = str(datetime.now().time())
    time = time.replace(':', '')
    time = time.replace('.', '')
    time = time.replace(' ', '')  # This will convert time and date into an int (2019-1-1 10:14.13456 = 201911101413456)

    very_large_random_number = str(randbelow(10**100))
    string = string + very_large_random_number + time

    return sha3_256(string.encode('utf-8')).hexdigest()  # Return out for string digested as sha_256, including
                                                            # time when creating and a very large random number
