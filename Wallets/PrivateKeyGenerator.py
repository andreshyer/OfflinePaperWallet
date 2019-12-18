from datetime import datetime
from hashlib import sha3_256
from secrets import randbelow


def NewPrivateKey(string, soft):
    if soft:
        return sha3_256(string.encode('utf-8')).hexdigest()  # Return output for string digested as sha_256

    time = str(datetime.now().time())
    time = time.replace(':', '')
    time = time.replace('.', '')  # This will convert time and date into an int (2019-1-1 10:14.13456 = 201911101413456)

    very_large_random_number = str(randbelow(10**100))
    string = string + very_large_random_number + time

    return sha3_256(string.encode('utf-8')).hexdigest()  # Return out for string digested as sha_256, including
                                                            # time when creating and a very large random number
